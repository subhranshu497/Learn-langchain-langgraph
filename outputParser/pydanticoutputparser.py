from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from torch import gt

load_dotenv()  # Load environment variables from .env file

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="The person's name")
    age: int = Field(gt=18, description="The person's age")
    city: str = Field(description="The city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
    template= 'Generate the name, age and city of a fictional {place} person \n {format_instructions}',
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser
final_res = chain.invoke({'place':'Indian'})
print("Final Result: ", final_res)

# prompt = template.invoke({'place':'Indian'})
# response = model.invoke(prompt)
# parsed_response = parser.parse(response.content)
# print("Parsed Response: ", parsed_response)