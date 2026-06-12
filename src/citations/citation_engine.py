from collections import OrderedDict


class CitationEngine:

    @staticmethod
    def generate(chunks):
        """
        Main method used by app.py
        """
        return CitationEngine.format_sources(chunks)

    @staticmethod
    def build_sources(chunks):

        sources = OrderedDict()

        for idx, chunk in enumerate(chunks, start=1):

            sources[idx] = {
                "source": chunk["source"],
                "page": chunk["page"],
                "chunk_id": chunk["chunk_id"]
            }

        return sources

    @staticmethod
    def format_sources(chunks):

        sources = CitationEngine.build_sources(chunks)

        source_lines = []

        for num, metadata in sources.items():

            source_lines.append(
                f"[{num}] {metadata['source']} | Page {metadata['page']}"
            )

        return "\n".join(source_lines)