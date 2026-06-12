import faiss
import pickle
import numpy as np
from pathlib import Path


class FAISSStore:

    def __init__(self):
        self.index = None

    def build_index(self, embeddings):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(
            dimension
        )

        self.index.add(
            embeddings.astype("float32")
        )

        return self.index

    def save_index(
        self,
        index_path="data/processed/faiss.index"
    ):
        faiss.write_index(
            self.index,
            index_path
        )

    def load_index(
        self,
        index_path="data/processed/faiss.index"
    ):
        self.index = faiss.read_index(
            index_path
        )

    def search(
        self,
        query_embedding,
        top_k=10
    ):

        scores, indices = self.index.search(
            np.array(
                [query_embedding]
            ).astype("float32"),
            top_k
        )

        return scores[0], indices[0]