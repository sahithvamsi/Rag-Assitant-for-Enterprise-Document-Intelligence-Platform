from sentence_transformers import SentenceTransformer
import numpy as np


class EmbeddingModel:

    def __init__(
        self,
        model_name="BAAI/bge-small-en-v1.5"
    ):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, chunks):

        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            show_progress_bar=True
        )

        return np.array(embeddings)

    def embed_query(self, query):

        embedding = self.model.encode(
            query,
            normalize_embeddings=True
        )

        return embedding