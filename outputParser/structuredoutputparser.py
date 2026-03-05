import os
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
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

# Define the response schema
response_schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the fictional person"),
    ResponseSchema(name="fact_2", description="Fact 2 about the fictional person"),
    ResponseSchema(name="fact_3", description="Fact 3 about the fictional person"),
]  

parser = StructuredOutputParser.from_response_schemas(response_schema)

test_prompt = PromptTemplate(
    template= 'give me three facts about a f{topic} \n {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = test_prompt | chat_model | parser
final_res = chain.invoke({'topic':'fictional person'})
print("Final Result: ", final_res)  

# prompt = test_prompt.invoke({'topic':'fictional person'})
# response = chat_model.invoke(prompt)
# parsed_response = parser.parse(response.content)
# print("Parsed Response: ", parsed_response)