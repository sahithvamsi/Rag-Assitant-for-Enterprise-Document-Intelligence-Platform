
🤖 DocuMind AI: Enterprise Document Intelligence Platform
Upload PDFs • Ask Questions • Get Source-Cited Answers using RAG, Hybrid Search, and LLMs.

Live Demo: https://ragproject345.streamlit.app/

📌 Overview
DocuMind AI is an enterprise-grade Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions about them.

The system combines:

Semantic Search using FAISS

Keyword Search using BM25

Hybrid Retrieval

Cross-Encoder Reranking

LLM-powered Answer Generation with Groq Llama 3.3 70B

Unlike traditional chatbots, DocuMind AI provides source-aware answers with citations, enabling users to verify information directly from uploaded documents.

✨ Features
✅ Upload PDF documents

✅ Extract and process document text

✅ Intelligent chunking with metadata preservation

✅ Semantic search using embeddings + FAISS

✅ Keyword retrieval using BM25

✅ Hybrid retrieval for improved accuracy

✅ CrossEncoder reranking

✅ LLM-generated answers

✅ Page-level citations

✅ Interactive Streamlit UI

✅ Display retrieved evidence chunks

🏗️ System Architecture
User Uploads PDF
        ↓
Document Parser
        ↓
Document Chunker
        ↓
Embedding Generation
        ↓
FAISS Index
        ↓
BM25 Index
        ↓
User Query
        ↓
Vector Search + BM25 Search
        ↓
Hybrid Search
        ↓
CrossEncoder Reranking
        ↓
Top Relevant Chunks
        ↓
Prompt Construction
        ↓
Groq LLM (Llama 3.3 70B)
        ↓
Answer Generation
        ↓
Source Citations + UI Display
🛠 Tech Stack
Frontend
Streamlit

Backend / RAG Pipeline
Python

NumPy

Pickle

Document Processing
PyMuPDF (fitz)

LangChain Text Splitters

Embedding Models
Sentence Transformers

BGE Embeddings

Retrieval
FAISS

BM25 (rank_bm25)

Reranking
CrossEncoder (ms-marco-MiniLM-L-6-v2)

LLM
Groq API

Llama 3.3 70B Versatile

📂 Project Structure
project/
│
├── app.py
│
├── src/
│   ├── ingestion/
│   │   ├── parser.py
│   │   └── chunker.py
│   │
│   ├── indexing/
│   │   ├── embeddings.py
│   │   ├── faiss_store.py
│   │   └── bm25_index.py
│   │
│   ├── retrieval/
│   │   ├── vector_search.py
│   │   ├── bm25_search.py
│   │   ├── hybrid_search.py
│   │   └── reranker.py
│   │
│   ├── llm/
│   │   ├── prompt.py
│   │   └── answer_generator.py
│   │
│   └── citations/
│       └── citation_engine.py
│
├── data/
├── requirements.txt
├── .env
└── README.md
⚙️ RAG Pipeline
Step 1: Document Parsing
Extract text and page information from uploaded PDFs.

docs = DocumentParser.parse(pdf_path)
Output:

{
    "source": "AI.pdf",
    "page": 1,
    "text": "..."
}
Step 2: Chunking
Large documents are split into smaller chunks.

chunks = chunker.chunk_documents(docs)
Each chunk contains metadata:

{
    "text": "...",
    "source": "AI.pdf",
    "page": 1,
    "chunk_id": 12
}
Step 3: Embedding Generation
Convert text into dense vector embeddings.

embeddings = embedder.embed_documents(chunks)
Example:

"Machine Learning"

↓

[0.12, 0.54, -0.77, ...]
Step 4: FAISS Indexing
Store embeddings for semantic retrieval.

faiss.IndexFlatIP()
Step 5: BM25 Indexing
Enable keyword-based search.

BM25Okapi()
Step 6: Hybrid Retrieval
Combine semantic and keyword search.

hybrid_score =
(vector_score * 0.6) +
(bm25_score * 0.4)
Step 7: CrossEncoder Reranking
Improve retrieval precision.

Input:

Top 30 chunks
Output:

Top 5 chunks
Step 8: Prompt Construction
Create structured context:

[Source 1]
File: AI.pdf
Page: 5
...
Step 9: LLM Generation
Generate answers using:

Llama 3.3 70B via Groq API
🎯 Example Workflow
Upload PDF
      ↓
Ask Question:
"What is Machine Learning?"
      ↓
Retrieve Relevant Chunks
      ↓
Rerank Results
      ↓
Generate Context
      ↓
LLM Answer
      ↓
Display Citations
🚀 Installation
Clone the repository:

git clone <repository-url>
cd project
Install dependencies:

pip install -r requirements.txt
Create .env file:

GROQ_API_KEY=your_api_key
Run the application:

streamlit run app.py
📈 Future Enhancements
Multi-document support

Persistent vector database

OCR support for scanned PDFs

Authentication and user management

Conversation memory

FastAPI backend

Cloud deployment on AWS/GCP/Azure

Docker support

💡 Key Learnings
Retrieval-Augmented Generation (RAG)

Vector Databases

Semantic Search

Hybrid Retrieval

Prompt Engineering

LLM Integration

Source Attribution

Streamlit Deployment

👨‍💻 Author
Sahith Vamsi Gandrala

Built as an end-to-end Enterprise Document Intelligence Platform demonstrating modern RAG architecture, hybrid retrieval, and LLM-powered document understanding.
