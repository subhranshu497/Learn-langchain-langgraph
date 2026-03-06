from langchain_openai import ChatOpenAI, OpenAI
from langchain_anthropic import Anthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnabeLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(..., description="The sentiment of the feedback")

promt1 = PromptTemplate(
    template="Classify the sentiments of the following text into positive or negative \n {feedback} \n {instructions}",
    input_variables=["feedback"],
    partial_variables={"instructions": "Respond with only the sentiment label without any explanation."}
)

prompt2 = PromptTemplate(
    template="Write an appropriate response to the positive feedback \n {feedback}",
    input_variables=["feedback"]
)   

prompt3 = PromptTemplate(
    template="Write an appropriate response to the negative feedback \n {feedback}",
    input_variables=["feedback"]
) 

classifier_chain = promt1 | model | parser2

#just to check the output of the classifier chain
result = classifier_chain.invoke({"feedback": "The product is amazing and I love it!"}).sentiment

print(result.content)

#branch chain
branch_chain = RunnableBranch(
    (lambda x:x['sentiment']=='positive', prompt2 | model | parser),
    (lambda x:x['sentiment']=='negative', prompt3 | model | parser),
    RunnabeLambda(lambda x: "Invalid sentiment")
)

chain = classifier_chain | branch_chain
result = chain.invoke({"feedback": "The product is amazing and I love it!"})
print(result)

chain.get_graph().print_ascii()