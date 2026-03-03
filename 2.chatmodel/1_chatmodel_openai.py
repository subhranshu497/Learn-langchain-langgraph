from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatOpenAI(model='gpt-4-0613')
response = chatModel.invoke("What is the capital of India?")
print(response.content)

