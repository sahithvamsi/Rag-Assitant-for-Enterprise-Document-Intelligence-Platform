# src/llm/answer_generator.py

import os

from groq import Groq
from dotenv import load_dotenv

from src.llm.prompt import SYSTEM_PROMPT

load_dotenv()


class AnswerGenerator:

    def __init__(self):

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def build_context(
        self,
        chunks
    ):

        context_parts = []

        for i, chunk in enumerate(chunks, start=1):

            context_parts.append(
                f"""
[Source {i}]
File: {chunk['source']}
Page: {chunk['page']}

{chunk['text']}
"""
            )

        return "\n".join(context_parts)

    def generate(
        self,
        question,
        chunks
    ):

        context = self.build_context(
            chunks
        )

        user_prompt = f"""
Question:
{question}

Context:
{context}

Instructions:

- Answer using ONLY the provided context.
- Give a complete explanation.
- Use citations such as [1], [2].
- Do not summarize chapter titles.
- Give the actual answer.
- If information is missing, say:
  "I could not find this information in the uploaded documents."
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.1,
            max_tokens=1000
        )

        return response.choices[0].message.content