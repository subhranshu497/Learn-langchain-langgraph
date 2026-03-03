import os
import warnings

# Suppress PyTorch warning before importing transformers
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
warnings.filterwarnings("ignore")

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Check if HuggingFace API token is set
hf_token = os.getenv("HF_TOKEN")
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm)
response = model.invoke("What is the capital of France?")
print(response.content)


