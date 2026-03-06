from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="Generat five interesting facts about {topic}.",
    input_variables=["topic"]   
)

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

parser = StrOutputParser()

chain = prompt | model | parser
chain.get_graph().render("chain_graph.png")
result = chain.invoke({"topic": "space exploration"})
print(result)