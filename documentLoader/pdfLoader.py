from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

loader = PyPDFLoader('SUBHRANSHU_MOHAPATRA_developer.pdf')
docs = loader.load()

print(len(docs))

#print(docs[0].page_content)
print(docs[1].metadata)