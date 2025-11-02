"""
pyATS + AEtest + LangChain Integration (Simplified)
---------------------------------------------------
1️⃣ Runs AEtest to execute "show ip interface brief" on all devices.
2️⃣ Saves outputs to text files.
3️⃣ Uses LangChain to summarize results.
"""

import os
from pathlib import Path
from pyats import aetest
from pyats.topology import loader

# 🔹 LangChain imports
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / "device_logs"
LOG_DIR.mkdir(exist_ok=True)

TESTBED_PATH = BASE_DIR / "testbed.yaml"
testbed = loader.load(str(TESTBED_PATH))

# ============================================================
# PYATS TEST SECTIONS
# ============================================================

class common_setup(aetest.CommonSetup):
    """Common setup: connect to all devices"""

    @aetest.subsection
    def connect_to_devices(self):
        testbed.connect()

    @aetest.subsection
    def loop_mark(self):
        aetest.loop.mark(MyTestcase, device_name=testbed.devices.keys())


class MyTestcase(aetest.Testcase):
    """TestCase: Run 'show ip interface brief' and save output"""

    @aetest.test
    def setup(self, device_name):
        self.device = testbed.devices[device_name]

    @aetest.test
    def capture_show_ip_interface_brief(self):
        """Execute command and save to log file"""
        output = self.device.execute("show ip interface brief")
        log_path = LOG_DIR / f"{self.device.name}_show_ip_int_brief.txt"
        with open(log_path, "w") as f:
            f.write(output)
        print(f"✅ Saved {self.device.name} output to {log_path}")


class common_cleanup(aetest.CommonCleanup):
    """Common cleanup: disconnect from devices"""

    @aetest.subsection
    def disconnect_from_devices(self):
        testbed.disconnect()


# ============================================================
# LANGCHAIN ANALYSIS SECTION
# ============================================================

def analyze_with_langchain():
    """Load show_ip outputs and summarize using LangChain"""
    print("\n🤖 Starting LangChain analysis...")

    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("❌ OPENAI_API_KEY not set!")

    # Combine all device logs into a single text file
    combined_path = LOG_DIR / "combined_logs.txt"
    with open(combined_path, "w") as outfile:
        for f in LOG_DIR.glob("*_show_ip_int_brief.txt"):
            outfile.write(f"\n\n=== {f.stem} ===\n")
            outfile.write(f.read_text())

    # Load with LangChain
    loader = TextLoader(str(combined_path))
    documents = loader.load()

    # Split with safe separator to prevent long chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )
    docs = splitter.split_documents(documents)
    print(f"✅ Split into {len(docs)} chunks")

    # Reset Chroma DB
    chroma_dir = LOG_DIR / "chroma_db"
    if chroma_dir.exists():
        import shutil
        shutil.rmtree(chroma_dir)
    chroma_dir.mkdir(exist_ok=True)

    # Embeddings + retriever
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(docs, embeddings, persist_directory=str(chroma_dir))
    retriever = db.as_retriever(search_kwargs={"k": 4})

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

    # Ask a single summary question
    query = "Summarize the 'show ip interface brief' results: which interfaces are up or down for each device?"
    print(f"\n🧠 Question: {query}")

    result = qa_chain.invoke({"query": query})
    print(f"\n💬 LangChain Summary:\n{result['result']}")


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":
    # Step 1️⃣: Run AEtest
    aetest.main()

    # Step 2️⃣: Analyze test results with LangChain
    analyze_with_langchain()
