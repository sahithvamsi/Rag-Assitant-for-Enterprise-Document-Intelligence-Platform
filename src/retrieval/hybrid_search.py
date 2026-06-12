class HybridSearcher:

    def __init__(
        self,
        vector_searcher,
        bm25_searcher
    ):
        self.vector_searcher = (
            vector_searcher
        )

        self.bm25_searcher = (
            bm25_searcher
        )

    def search(
        self,
        query,
        top_k=50,
        vector_weight=0.6,
        bm25_weight=0.4
    ):

        vector_results = (
            self.vector_searcher.search(
                query,
                top_k
            )
        )

        bm25_results = (
            self.bm25_searcher.search(
                query,
                top_k
            )
        )

        combined = {}

        # vector scores
        for result in vector_results:

            key = result["chunk_id"]

            combined[key] = result.copy()

            combined[key]["hybrid_score"] = (
                result["score"]
                * vector_weight
            )

        # bm25 scores
        for result in bm25_results:

            key = result["chunk_id"]

            if key not in combined:

                combined[key] = result.copy()

                combined[key][
                    "hybrid_score"
                ] = 0

            combined[key]["hybrid_score"] += (
                result["score"]
                * bm25_weight
            )

        ranked = sorted(
            combined.values(),
            key=lambda x: x["hybrid_score"],
            reverse=True
        )

        return ranked[:top_k]