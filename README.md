# Domain-Specific Q&A Chatbot

A smart chatbot that answers questions based on uploaded PDF documents.

## Features
- Extracts data from PDFs
- Answers user queries using AI (LangChain + Hugging Face)
- Simple PyTorch model placeholder for tuning
- Web interface with Streamlit
- Shows source documents with answers

## Run the App
1. Install requirements:
```
pip install -r requirements.txt
```
2. Place your PDFs in `sample_pdfs/`
3. Run the app:
```
streamlit run app.py
```
