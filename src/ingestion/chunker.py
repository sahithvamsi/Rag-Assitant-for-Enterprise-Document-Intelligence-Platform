from typing import List, Dict

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from src.ingestion.metadata import (
    MetadataManager
)


class DocumentChunker:

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):

        self.splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )
        )

    def chunk_documents(
        self,
        documents: List[Dict]
    ):

        chunks = []

        chunk_id = 0

        for doc in documents:

            split_chunks = self.splitter.split_text(
                doc["text"]
            )

            for chunk in split_chunks:

                metadata = (
                    MetadataManager.create_metadata(
                        source=doc["source"],
                        page=doc["page"],
                        chunk_id=chunk_id
                    )
                )

                chunks.append(
                    {
                        "text": chunk,
                        **metadata
                    }
                )

                chunk_id += 1

        return chunks