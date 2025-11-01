import os
import shutil
from pathlib import Path
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# 🔹 Ensure OpenAI API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise EnvironmentError("❌ OPENAI_API_KEY environment variable not set!")

# 🔹 Set paths
base_dir = Path(__file__).parent
text_path = base_dir / "logging.txt"
chroma_dir = base_dir / "chroma_temp"

# 🔹 Check file existence
print(f"📁 Working directory: {base_dir}")
print(f"📄 Log file exists: {text_path.exists()}")

if not text_path.exists():
    raise FileNotFoundError(f"❌ File not found: {text_path}")

# 1️⃣ Load documents
loader = TextLoader(str(text_path))
documents = loader.load()
print(f"✅ Loaded {len(documents)} document(s)")

# 2️⃣ Split into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)
print(f"✅ Split into {len(docs)} chunks")

# 🔹 Show sample text
print("🔍 Sample text chunk:\n", docs[0].page_content[:250], "\n---")

# 3️⃣ Reset Chroma vector database each run
shutil.rmtree(chroma_dir, ignore_errors=True)
chroma_dir.mkdir(exist_ok=True)

# 4️⃣ Create embeddings and vectorstore
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embeddings, persist_directory=str(chroma_dir))

# 5️⃣ Create retriever
retriever = db.as_retriever(search_kwargs={"k": 4})

# 6️⃣ Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 7️⃣ Create RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

# 8️⃣ Ask question
query = "What are the most important messages in the log file in summary?"
print(f"\n🧠 Question: {query}")

result = qa_chain.invoke({"query": query})
print(f"💬 Answer:\n{result['result']}")
