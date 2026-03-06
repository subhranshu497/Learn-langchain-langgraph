from langchain_openai import ChatOpenAI, OpenAI
from langchain_anthropic import Anthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
load_dotenv()

model1 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)
model2 = ChatOpenAI(model="claude-3-5-sonnet", temperature=0.9)

prompt1 = PromptTemplate(
    template="Generate a short and simple notes from the following text \n {text}",
    input_variables=["text"]
)
prompt2 = PromptTemplate(
    template="Generate five short question and answers from the following text \n {text}",
    input_variables=["text"]
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single comprehensive summary \n Notes: {notes} \n Quiz: {quiz}",
    input_variables=["notes", "quiz"]
)
parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

result = chain.invoke({"text": "The history of artificial intelligence (AI) dates back to the mid-20th century, with the term 'artificial intelligence' being coined in 1956 at a conference at Dartmouth College. Early AI research focused on symbolic reasoning and problem-solving, but progress was slow due to limited computational power and data. In the 1980s, the rise of machine learning and neural networks led to significant advancements in AI capabilities. The 21st century has seen an explosion of AI applications, from natural language processing and computer vision to autonomous vehicles and healthcare. Today, AI continues to evolve rapidly, with ongoing research in areas such as deep learning, reinforcement learning, and ethical considerations surrounding AI deployment."})
print(result)   

chain.get_graph().print_ascii()
