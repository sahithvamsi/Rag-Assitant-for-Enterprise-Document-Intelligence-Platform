import pickle
from rank_bm25 import BM25Okapi


class BM25Indexer:

    def __init__(self):

        self.bm25 = None
        self.corpus = None

    def build(self, chunks):

        self.corpus = chunks

        tokenized_docs = [
            chunk["text"].split()
            for chunk in chunks
        ]

        self.bm25 = BM25Okapi(
            tokenized_docs
        )

        return self.bm25

    def search(
        self,
        query,
        top_k=10
    ):

        tokenized_query = query.split()

        scores = self.bm25.get_scores(
            tokenized_query
        )

        ranked = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked[:top_k]

    def save(
        self,
        path="data/processed/bm25.pkl"
    ):

        with open(path, "wb") as f:
            pickle.dump(self.bm25, f)

    def load(
        self,
        path="data/processed/bm25.pkl"
    ):

        with open(path, "rb") as f:
            self.bm25 = pickle.load(f)