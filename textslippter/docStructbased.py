from langchain_text_splitters import RecursiveCharacterTextSplitter, PythonCodeTextSplitter, Language

text = """from langchain_google_genai import ChatGoogleGenAI
from dotenv import load_dotenv 
load_dotenv()

chatModel = ChatGoogleGenAI(model='gemini-2.0-pro')
response = chatModel.invoke("What is the capital of India?")
print(response.content)"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language= Language.PYTHON,
    chunk_size = 300,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)