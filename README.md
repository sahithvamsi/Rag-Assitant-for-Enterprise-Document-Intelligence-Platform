# 🤖 DocuMind AI — Enterprise Document Intelligence Platform

> Upload PDFs • Ask Questions • Get Source-Cited Answers using RAG, Hybrid Search, and LLMs.

🌐 **Live Demo:** https://ragproject345.streamlit.app/

---

## 📌 Overview

DocuMind AI is an enterprise-grade **Retrieval-Augmented Generation (RAG)** platform that enables users to upload PDF documents and interact with them using natural language queries.

Instead of relying only on an LLM's internal knowledge, the system retrieves relevant information directly from uploaded documents and generates accurate, source-grounded answers with citations.

The platform combines:

- Semantic Search using **FAISS**
- Keyword Search using **BM25**
- Hybrid Retrieval
- Cross-Encoder Reranking
- LLM-powered Answer Generation using **Groq Llama 3.3 70B**

This approach reduces hallucinations and improves answer reliability by grounding responses in document content.

---

## ✨ Features

- ✅ Upload PDF documents
- ✅ Automatic text extraction and preprocessing
- ✅ Intelligent chunking with metadata preservation
- ✅ Dense vector embeddings for semantic search
- ✅ FAISS-based vector retrieval
- ✅ BM25 keyword retrieval
- ✅ Hybrid search for improved recall
- ✅ CrossEncoder reranking for better precision
- ✅ LLM-powered answer generation
- ✅ Page-level citations
- ✅ Interactive Streamlit interface
- ✅ Retrieved evidence visualization

---

## 🏗️ System Architecture

```text
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
```

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend / Core Logic
- Python
- NumPy
- Pickle

### Document Processing
- PyMuPDF (`fitz`)
- LangChain Text Splitters

### Embedding Models
- Sentence Transformers
- BGE Embeddings

### Retrieval
- FAISS
- BM25 (`rank_bm25`)

### Reranking
- CrossEncoder (`ms-marco-MiniLM-L-6-v2`)

### LLM
- Groq API
- Llama 3.3 70B Versatile

---

## 📂 Project Structure

```text
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
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone <repository-url>
cd project
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Environment File

```env
GROQ_API_KEY=your_api_key
```

### Run Application

```bash
streamlit run app.py
```

---

## 📈 Future Enhancements

- Multi-document support
- Persistent vector databases
- OCR for scanned PDFs
- Authentication & authorization
- Conversation memory
- FastAPI backend
- Docker deployment
- AWS/GCP/Azure deployment
- Multi-user support

---

## 👨‍💻 Author

**Sahith Vamsi Gandrala**

Built as an end-to-end **Enterprise Document Intelligence Platform** showcasing modern AI system design using **RAG, Hybrid Retrieval, CrossEncoder Reranking, and LLM-powered document understanding**.
