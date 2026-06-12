from src.indexing.embeddings import EmbeddingModel


class VectorSearcher:

    def __init__(
        self,
        faiss_store,
        embedding_model,
        chunks
    ):
        self.faiss_store = faiss_store
        self.embedding_model = embedding_model
        self.chunks = chunks

    def search(
        self,
        query,
        top_k=20
    ):

        query_embedding = (
            self.embedding_model.embed_query(
                query
            )
        )

        scores, indices = (
            self.faiss_store.search(
                query_embedding,
                top_k
            )
        )

        results = []

        for score, idx in zip(
            scores,
            indices
        ):

            if idx < 0:
                continue

            chunk = self.chunks[idx].copy()

            chunk["score"] = float(score)

            results.append(chunk)

        return results