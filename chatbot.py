from transformers import pipeline
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage, ChatMessage

# 1. Load a text-generation model from Hugging Face
transformers = pipeline(
    "text-generation",
    model="bigscience/bloom-560m",
    max_new_tokens=100
)

print("Chatbot ready! Type 'exit' to quit.\n")

chat_history = []

# 2. Simple chat loop
while True:
    user_input = input("You: ")
    chat_history.append(f"User: {user_input}")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    # 3️. Generate a response
    response = generator(chat_history, max_length=100, num_return_sequences=1)
    chat_history.append(f"AI: {response[0]['generated_text']}")
    print("AI: ", response[0]['generated_text'])