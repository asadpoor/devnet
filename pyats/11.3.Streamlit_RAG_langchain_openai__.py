import os
from pathlib import Path
import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate  # added for log-focused prompt

# --------------------------
# 🧠 Initialization
# --------------------------
st.set_page_config(page_title="Log File QA", page_icon="🧾", layout="wide")
st.title("🧾 Log File Question Answering App")

# Ensure OpenAI API key is set
if not os.getenv("OPENAI_API_KEY"):
    st.error("❌ OPENAI_API_KEY environment variable not set!")
    st.stop()

base_dir = Path(__file__).parent
text_path = base_dir / "logging.txt"

if not text_path.exists():
    st.error(f"❌ File not found: {text_path}")
    st.stop()

# --------------------------
# 📄 Load and Prepare Docs
# --------------------------
with st.spinner("Loading and processing log file..."):
    loader = TextLoader(str(text_path))
    documents = loader.load()

    # Slightly larger chunks
    text_splitter = CharacterTextSplitter(chunk_size=1500, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    # Use in-memory Chroma (remove persistent DB to avoid readonly error)
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(docs, embeddings)  # no persist_directory
    retriever = db.as_retriever(search_kwargs={"k": 6})  # retrieve more chunks

    # Log-focused prompt
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are an expert engineer analyzing log files. Here are excerpts from a log:

{context}

Highlight any errors or warnings and answer the user question clearly.

Question: {question}
Answer:
"""
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

st.success(f"✅ Log file loaded with {len(docs)} text chunks.")

# --------------------------
# 💬 User Input
# --------------------------
st.markdown("### Ask a question about the log file:")
user_query = st.text_area("Enter your question here", placeholder="e.g. What are the key errors or warnings?")

if st.button("Ask"):
    if user_query.strip():
        with st.spinner("Analyzing log and generating answer..."):
            result = qa_chain.invoke({"query": user_query})
            st.subheader("💬 Answer:")
            st.write(result["result"])
    else:
        st.warning("⚠️ Please enter a question before clicking *Ask*.")

# --------------------------
# 🧠 Sidebar Information
# --------------------------
with st.sidebar:
    st.header("About")
    st.write("""
    This app uses **LangChain**, **OpenAI GPT**, and **Chroma** to answer
    questions about your log file.

    - File: `logging.txt`  
    - Embeddings: `OpenAIEmbeddings`  
    - Model: `gpt-4o-mini`
    """)
