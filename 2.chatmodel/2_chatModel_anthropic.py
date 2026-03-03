from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

chatModel = ChatAnthropic(model='Claude Haiku 4.5')
response = chatModel.invoke("What is the capital of India?")
print(response.content)