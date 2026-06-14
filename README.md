DocuMind AI — Enterprise Document Intelligence Platform
Upload PDFs • Ask Questions • Get Source-Cited Answers using RAG, Hybrid Search, and LLMs

🌐 Live Demo: https://ragproject345.streamlit.app/

📌 Overview
DocuMind AI is an enterprise-grade Retrieval-Augmented Generation (RAG) platform that enables users to upload PDF documents and interact with them using natural language queries.

Instead of relying only on an LLM's internal knowledge, the system retrieves relevant information directly from uploaded documents and generates accurate, source-grounded answers with citations.

The platform combines:

Semantic Search using FAISS

Keyword Search using BM25

Hybrid Retrieval

Cross-Encoder Reranking

LLM-powered Answer Generation using Groq Llama 3.3 70B

This approach reduces hallucinations and improves answer reliability by grounding responses in document content.

✨ Features
✅ Upload PDF documents

✅ Automatic text extraction and preprocessing

✅ Intelligent chunking with metadata preservation

✅ Dense vector embeddings for semantic search

✅ FAISS-based vector retrieval

✅ BM25 keyword retrieval

✅ Hybrid search for improved recall

✅ CrossEncoder reranking for better precision

✅ LLM-powered answer generation

✅ Page-level citations

✅ Interactive Streamlit interface

✅ Retrieved evidence visualization

User Uploads PDF
        ↓
Document Parser
        ↓
Document Chunker
        ↓
Embedding Generation
        ↓
FAISS Vector Index
        ↓
BM25 Keyword Index
        ↓
User Query
        ↓
Vector Search + BM25 Search
        ↓
Hybrid Retrieval
        ↓
CrossEncoder Reranking
        ↓
Top Relevant Chunks
        ↓
Prompt Construction
        ↓
Groq Llama 3.3 70B
        ↓
Answer Generation
        ↓
Source Citations + UI Display
Frontend
Streamlit

Backend / Core Logic
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
⚙️ End-to-End RAG Pipeline
Step 1: Document Parsing
The uploaded PDF is parsed page by page.

docs = DocumentParser.parse(pdf_path)
Output:

{
    "source": "AI.pdf",
    "page": 1,
    "text": "Machine Learning is ..."
}
Step 2: Document Chunking
Large documents are split into smaller chunks.

chunks = chunker.chunk_documents(docs)
Each chunk contains metadata:

{
    "text": "...",
    "source": "AI.pdf",
    "page": 1,
    "chunk_id": 12
}
Why chunking?
LLM context windows are limited.

Smaller chunks improve retrieval accuracy.

Metadata enables citations.

Step 3: Embedding Generation
Text chunks are converted into dense vector representations.

embeddings = embedder.embed_documents(chunks)
Example:

"Machine Learning"

↓

[0.12, 0.54, -0.77, ...]
Step 4: FAISS Indexing
Embeddings are stored in a FAISS vector database.

faiss.IndexFlatIP()
Purpose:

Fast semantic similarity search

Efficient nearest-neighbor retrieval

Step 5: BM25 Indexing
Keyword-based retrieval is built using BM25.

BM25Okapi()
Purpose:

Exact keyword matching

Better handling of IDs, codes, and technical terms

Step 6: Hybrid Retrieval
Combine semantic and keyword search.

hybrid_score =
(vector_score * 0.6) +
(bm25_score * 0.4)
Why Hybrid Search?

FAISS captures semantics

BM25 captures exact keywords

Together they improve retrieval quality

Step 7: CrossEncoder Reranking
Initial retrieval returns:

Top 30 chunks
The CrossEncoder reranks them based on query relevance.

Output:

Top 5 most relevant chunks
This improves answer precision.

Step 8: Context Construction
Retrieved chunks are converted into structured context.

Example:

[Source 1]
File: AI.pdf
Page: 5

Machine Learning is a subset of AI.
Step 9: LLM Answer Generation
The context and user question are sent to:

Groq Llama 3.3 70B
Prompt Example:

Question:
What is Machine Learning?

Context:
[Source 1]
...
The model generates grounded answers with citations.

🎯 Example Workflow
Upload PDF
      ↓
Ask Question:
"What is Machine Learning?"
      ↓
Retrieve Relevant Chunks
      ↓
Hybrid Search
      ↓
CrossEncoder Reranking
      ↓
Build Context
      ↓
Generate Answer
      ↓
Display Citations
🚀 Installation
Clone Repository
git clone <repository-url>
cd project
Install Dependencies
pip install -r requirements.txt
Create Environment File
GROQ_API_KEY=your_api_key
Run Application
streamlit run app.py
📊 Why This Architecture?
Component	Purpose
FAISS	Semantic Search
BM25	Keyword Search
Hybrid Retrieval	Better Recall
CrossEncoder	Better Precision
Groq LLM	Answer Generation
Streamlit	User Interface
🔥 Key Technical Highlights
Retrieval-Augmented Generation (RAG)

Hybrid Search Architecture

Vector Databases

Prompt Engineering

CrossEncoder Reranking

Source Attribution

LLM Integration

Document Intelligence Systems

📈 Future Enhancements
Multi-document support

Persistent vector databases

OCR for scanned PDFs

Authentication & authorization

Conversation memory

FastAPI backend

Docker deployment

AWS/GCP/Azure deployment

Real-time indexing

Multi-user support

🎓 Key Learnings
This project demonstrates practical experience with:

Large Language Models (LLMs)

Retrieval-Augmented Generation (RAG)

Semantic Search

Vector Databases

Information Retrieval

Prompt Engineering

End-to-End ML System Design

Production AI Applications

👨‍💻 Author
Sahith Vamsi Gandrala

Built as an end-to-end Enterprise Document Intelligence Platform showcasing modern AI system design using RAG, Hybrid Retrieval, CrossEncoder Reranking, and LLM-powered document understanding.
