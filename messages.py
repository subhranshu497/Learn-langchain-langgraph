from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage, ChatMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os   
load_dotenv()

# Example usage
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about LangChain.")
]
response = model.invoke(messages)
messages.append(AIMessage(content=response.content))

print(messages)