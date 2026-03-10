from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence
load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Now, explain the joke you just wrote.",
    input_variables=[]
) 

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

parser = StrOutputParser()

chain = RunnableSequence(
        prompt1,
        model,
        parser,
        prompt2,
        model,
        parser
)

print(chain.invoke({"topic": "chickens crossing the road"}))