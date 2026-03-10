from langchain_community.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader, WebBaseLoader
from langchain_openai import OpenAI, ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

url = ""

loader = WebBaseLoader(url)
docs = loader.load()
model = ChatOpenAI()

prompt = PromptTemplate(
    template="Write a summary for the following \n{poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

print(docs[0].page_content)