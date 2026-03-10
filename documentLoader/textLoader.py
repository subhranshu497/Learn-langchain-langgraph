from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAI,ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template="Write a summary for the following \n{poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricketPoem.txt.rtf', encoding='utf-8')
docs = loader.load()
print(docs)
print(type(docs))
print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | parser

chain.invoke({'poem':docs[0].page_content})