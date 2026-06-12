import streamlit as st
import tempfile
import os

from src.ingestion.parser import DocumentParser
from src.ingestion.chunker import DocumentChunker

from src.indexing.embeddings import EmbeddingModel
from src.indexing.faiss_store import FAISSStore
from src.indexing.bm25_index import BM25Indexer

from src.retrieval.vector_search import VectorSearcher
from src.retrieval.bm25_search import BM25Searcher
from src.retrieval.hybrid_search import HybridSearcher
from src.retrieval.reranker import CrossEncoderReranker

from src.llm.answer_generator import AnswerGenerator
from src.citations.citation_engine import CitationEngine


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.hero {
    padding: 30px;
    border-radius: 20px;
    background: linear-gradient(
        135deg,
        #2563EB,
        #7C3AED
    );
    color: white;
    margin-bottom: 25px;
}

.answer-card {
    background: #111827;
    padding: 20px;
    border-radius: 15px;
    color: white;
}

.stButton > button {
    width: 100%;
    height: 50px;
    border-radius: 12px;
    background: #2563EB;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background: #1D4ED8;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🤖 DocuMind AI")

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    st.markdown("---")

    st.success(
        "FAISS + BM25 + CrossEncoder + Groq"
    )

    st.markdown("---")

    st.info(
        "Upload a PDF and ask questions."
    )

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero">

<h1>🤖 DocuMind AI</h1>

<h4>
Enterprise Document Intelligence Platform
</h4>

<p>
Upload PDFs • Ask Questions • Get Cited Answers
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# QUESTION INPUT
# --------------------------------------------------

query = st.text_input(
    "Ask a question about your document"
)

ask_button = st.button(
    "🚀 Generate Answer"
)

# --------------------------------------------------
# RAG PIPELINE FUNCTION
# --------------------------------------------------

def run_rag(pdf_path, pdf_name, query):

    # STEP 1
    docs = DocumentParser.parse(
        pdf_path
    )

    # STEP 2
    chunker = DocumentChunker()

    chunks = chunker.chunk_documents(
        docs
    )

    # preserve original filename

    for chunk in chunks:
        chunk["source"] = pdf_name

    # STEP 3
    embedder = EmbeddingModel()

    embeddings = embedder.embed_documents(
        chunks
    )

    # STEP 4
    faiss_store = FAISSStore()

    faiss_store.build_index(
        embeddings
    )

    # STEP 5
    bm25 = BM25Indexer()

    bm25.build(
        chunks
    )

    # STEP 6
    vector_searcher = VectorSearcher(
        faiss_store,
        embedder,
        chunks
    )

    bm25_searcher = BM25Searcher(
        bm25,
        chunks
    )

    hybrid = HybridSearcher(
        vector_searcher,
        bm25_searcher
    )
        # STEP 7
    results = hybrid.search(
        query,
        top_k=30
    )

    # STEP 8
    reranker = CrossEncoderReranker()

    top_chunks = reranker.rerank(
        query,
        results,
        top_k=5
    )

    # STEP 9
    generator = AnswerGenerator()

    answer = generator.generate(
        query,
        top_chunks
    )

    return answer, top_chunks


# --------------------------------------------------
# EXECUTION
# --------------------------------------------------

if uploaded_file and ask_button:

    with st.spinner(
        "Analyzing document..."
    ):

        # Save uploaded PDF

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as tmp:

            tmp.write(
                uploaded_file.read()
            )

            pdf_path = tmp.name

        pdf_name = uploaded_file.name

        answer, top_chunks = run_rag(
            pdf_path,
            pdf_name,
            query
        )

    st.success(
        "Analysis Complete"
    )

    # ----------------------------------------
    # ANSWER + SOURCES LAYOUT
    # ----------------------------------------

    col1, col2 = st.columns(
        [3, 1]
    )

    with col1:

       st.subheader("💬 Answer")

       st.info(answer)

    with col2:

        st.subheader("📚 Sources")

        shown = set()

        for chunk in top_chunks:

            key = (
                chunk["source"],
                chunk["page"]
            )

            if key not in shown:

                shown.add(key)

                st.info(
                    f"""
📄 {chunk['source']}

Page {chunk['page']}
"""
                )

    st.markdown("---")

    st.subheader(
        "🔍 Retrieved Chunks"
    )

    for i, chunk in enumerate(
        top_chunks,
        start=1
    ):

        with st.expander(
            f"Chunk {i} | Page {chunk['page']}"
        ):

            st.write(
                chunk["text"]
            )

elif ask_button and not uploaded_file:

    st.warning(
        "Please upload a PDF first."
    )