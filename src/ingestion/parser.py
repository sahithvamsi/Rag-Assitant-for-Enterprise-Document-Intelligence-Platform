from pathlib import Path
from typing import List, Dict

import fitz  # PyMuPDF
from docx import Document
from odf.opendocument import load
from odf import text as odf_text


class DocumentParser:

    @staticmethod
    def parse_pdf(file_path: str) -> List[Dict]:

        documents = []

        pdf = fitz.open(file_path)

        for page_num in range(len(pdf)):

            page = pdf.load_page(page_num)

            text = page.get_text()

            documents.append(
                {
                    "source": Path(file_path).name,
                    "page": page_num + 1,
                    "text": text
                }
            )

        pdf.close()

        return documents

    @staticmethod
    def parse_docx(file_path: str) -> List[Dict]:

        doc = Document(file_path)

        text = "\n".join(
            para.text for para in doc.paragraphs
        )

        return [
            {
                "source": Path(file_path).name,
                "page": 1,
                "text": text
            }
        ]

    @staticmethod
    def parse_txt(file_path: str) -> List[Dict]:

        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            text = f.read()

        return [
            {
                "source": Path(file_path).name,
                "page": 1,
                "text": text
            }
        ]

    @staticmethod
    def parse_odt(file_path: str) -> List[Dict]:

        doc = load(file_path)

        paragraphs = doc.getElementsByType(
            odf_text.P
        )

        text = "\n".join(
            p.firstChild.data
            for p in paragraphs
            if p.firstChild
        )

        return [
            {
                "source": Path(file_path).name,
                "page": 1,
                "text": text
            }
        ]

    @staticmethod
    def parse(file_path: str):

        suffix = Path(file_path).suffix.lower()

        if suffix == ".pdf":
            return DocumentParser.parse_pdf(file_path)

        elif suffix == ".docx":
            return DocumentParser.parse_docx(file_path)

        elif suffix == ".txt":
            return DocumentParser.parse_txt(file_path)

        elif suffix == ".odt":
            return DocumentParser.parse_odt(file_path)

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )