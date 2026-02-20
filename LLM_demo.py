from langchain_ollama import OllamaLLM

#initialize the Ollama LLM
llm = OllamaLLM(model="llama3")

#generate a response
result = llm.invoke("Who is Virat Kohli?")

print(result)
