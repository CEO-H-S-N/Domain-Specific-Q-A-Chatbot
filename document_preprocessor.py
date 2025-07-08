import os
import fitz  # PyMuPDF
from langchain.docstore.document import Document

def load_pdfs(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            filepath = os.path.join(folder_path, filename)
            pdf = fitz.open(filepath)
            for page_num in range(len(pdf)):
                text = pdf[page_num].get_text()
                docs.append(Document(page_content=text, metadata={"source": filename, "page": page_num}))
    return docs
