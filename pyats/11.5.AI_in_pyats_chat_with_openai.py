import os
import yaml
import logging
from rich import print
from pyats import aetest
from dotenv import load_dotenv
from pyats.log.utils import banner
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from pyats.topology import loader

# Load the testbed from the YAML file
testbed = loader.load("testbed.yaml")

# Get logger for script
log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO to capture logs

# Instantiate openAI client
load_dotenv()

# Load the API keys from an environment variable or secure source
openai_api_key = os.getenv("OPENAI_API_KEY")

# Instantiate the LLM with gpt-3.5-turbo
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

# AT Test Setup
class common_setup(aetest.CommonSetup):
    """Common Setup section"""

    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect()

    @aetest.subsection
    def loop_mark(self, testbed):
        aetest.loop.mark(Show_Run_Langchain, device_name=testbed.devices)

# Test Case
class Show_Run_Langchain(aetest.Testcase):
    """pyATS and AI"""

    @aetest.test
    def setup(self, testbed, device_name):
        """Testcase Setup section"""
        # Set current device in loop as self.device
        self.device = testbed.devices[device_name]

    @aetest.test
    def get_raw_config(self):
        self.raw_config = self.device.execute("show run")
        log.info(f"Raw configuration fetched from device {self.device.alias}")

    @aetest.test
    def create_file(self):
        with open(f'{self.device.alias}_Show_Run.txt', 'w') as f:
            f.write(self.raw_config)
        log.info(f"Configuration saved to file: {self.device.alias}_Show_Run.txt")

    @aetest.test
    def load_text(self):
        self.loader = TextLoader(f'{self.device.alias}_Show_Run.txt')
        log.info(f"Loaded text from file: {self.device.alias}_Show_Run.txt")

    @aetest.test
    def split_into_pages(self):
        self.pages = self.loader.load_and_split()

        # Create a text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=300,
            length_function=len,
        )
        log.info(f"Split text into pages.")

    @aetest.test
    def split_pages_into_chunks(self):
        self.docs = self.text_splitter.split_documents(self.pages)
        log.info(f"Split pages into chunks. Number of chunks: {len(self.docs)}")

    @aetest.test
    def store_in_chroma(self):
        embeddings = OpenAIEmbeddings()
        self.vectordb = Chroma.from_documents(self.docs, embedding=embeddings)
        self.vectordb.persist()
        log.info("Stored documents in ChromaDB.")

    @aetest.test
    def setup_conversation_memory(self):
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        log.info("Setup conversation memory.")

    @aetest.test
    def setup_conversation_retrieval_chain(self):
        self.qa = ConversationalRetrievalChain.from_llm(
            llm,
            self.vectordb.as_retriever(search_kwargs={"k": 10}),
            memory=self.memory
        )
        log.info("Setup conversational retrieval chain.")

    @aetest.test
    def chat_with_show_run(self):
        try:
            # Load questions from the YAML file
            with open("show_run_questions.yaml", 'r') as file:
                data = yaml.safe_load(file)
                questions = data['questions']
            log.info(f"Loaded questions from show_run_questions.yaml.")

            # Open a file in write mode
            with open("Show_Run_Q_A.txt", 'w') as file:
                for question in questions:
                    log.info(f"Asking question: {question}")
                    result = self.qa.run(question)
                    log.info(f"Answer: {result}")

                    # Write question and answers to the file
                    file.write(question + '\n')
                    file.write(f"This is from Conversational Retrieval Chain using ChromaDB\n{result}\n")
                    file.write('-' * 80 + '\n')  # Write a separator line for clarity

                log.info("All questions and answers written to Show_Run_Q_A.txt.")
        except Exception as e:
            log.error(f"Error in chatting with show run: {str(e)}")

class CommonCleanup(aetest.CommonCleanup):

    @aetest.subsection
    def disconnect_from_devices(self, testbed):
        testbed.disconnect()


# for running as its own executable
if __name__ == '__main__':
    aetest.main(testbed=testbed)
