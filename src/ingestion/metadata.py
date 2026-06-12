from datetime import datetime


class MetadataManager:

    @staticmethod
    def create_metadata(
        source: str,
        page: int,
        chunk_id: int
    ):

        return {
            "source": source,
            "page": page,
            "chunk_id": chunk_id,
            "timestamp": datetime.utcnow().isoformat()
        }