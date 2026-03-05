import os
from langchain_core.output_parsers import JsonOutputParser
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

parser = JsonOutputParser()

template1 = PromptTemplate(
    template= 'give me the name, age and city of a fictional person \n {format_insructions}',
    input_variables=[],
    partial_variables={'format_insructions': parser.get_format_instructions()}
)

chain = template1 | chat_model | parser
final_res = chain.invoke({})
print("Final Result: ", final_res)