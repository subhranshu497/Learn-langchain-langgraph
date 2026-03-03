from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv 
load_dotenv()

chatModel = ChatGoogleGenAI(model='gemini-2.0-pro')
response = chatModel.invoke("What is the capital of India?")
print(response.content)