import os
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate

load_dotenv()  # Load environment variables from .env file

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

# 3. Wrap it in the Chat Interface
chat_model = ChatHuggingFace(llm=llm)

#first prompt
template1 = PromptTemplate(
    template= 'Write a detailed report on {topic}',
    input_variables=['topic']
)

#second prompt

template2 = PromptTemplate(
    template= 'Write a five line summary on following {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | chat_model | parser | template2 | chat_model | parser

result = chain.invoke({'topic':'Climate Change'})
print("Final Result: ", result)

