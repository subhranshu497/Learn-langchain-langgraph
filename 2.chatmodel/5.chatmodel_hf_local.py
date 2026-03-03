from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    repo_id="google/gemma-3-1b-it",
    task="text-generation",
    pipeline_kwargs={
        "max_length": 100, 
        "temperature": 0.7}
)
model = ChatHuggingFace(llm=llm)
response = model.invoke("What is the capital of France?")
print(response.content)