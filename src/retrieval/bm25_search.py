class BM25Searcher:

    def __init__(
        self,
        bm25_index,
        chunks
    ):
        self.bm25_index = bm25_index
        self.chunks = chunks

    def search(
        self,
        query,
        top_k=20
    ):

        ranked = self.bm25_index.search(
            query,
            top_k
        )

        results = []

        for idx, score in ranked:

            chunk = self.chunks[idx].copy()

            chunk["score"] = float(score)

            results.append(chunk)

        return results