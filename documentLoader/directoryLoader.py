from langchain_community.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
#eager loading by default
loader = DirectoryLoader(
    path = "sample",
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)


docs = loader.load()


print(len(docs))

