import streamlit as st
from ingest import load_pdfs
from qa_chain import ask_question

st.title("📄 Domain-Specific Q&A Chatbot")
st.markdown("Upload PDFs and ask questions based on their content.")

pdf_dir = "sample_pdfs"
docs = load_pdfs(pdf_dir)

if docs:
    question = st.text_input("Ask a question:")
    if question:
        answer, sources = ask_question(docs, question)
        st.subheader("Answer:")
        st.write(answer)
        st.subheader("Sources:")
        for src in sources:
            st.code(src.page_content[:500])
else:
    st.warning("No PDFs found. Add files to sample_pdfs/")
