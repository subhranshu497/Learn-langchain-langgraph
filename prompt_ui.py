from langchain_community.chat_models import ChatOllama
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_huggingface import HuggingFaceEndpoint
import streamlit as st


st.header("Research Tool")
user_input = st.text_input("Enter your prompt here")

llm = HuggingFacePipeline.from_model_id(
    model_id="google/gemma-3-1b-it",
    task="text-generation",
    pipeline_kwargs={
        "max_length": 100, 
        "temperature": 0.7}
)
model = ChatHuggingFace(llm=llm)
response = model.invoke("Explain the concept of quantum computing in simple terms.")
print(response.content)

if st.button('Summarize'):
    result = model(user_input)
    st.write(result.content)

    