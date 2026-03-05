from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage, ChatMessage

# Define a chat prompt template with a placeholder for messages
chat_template = ChatPromptTemplate(
    [
        ('system', 'You are a helpful customer support agent.'),
        MessagesPlaceholder(variable_name='conversation_history'),
        ('human', '{query}')
    ]
)

#load conversation history
conversation_history = [
    {'role': 'human', 'content': 'I have an issue with my order.'},
    {'role': 'ai', 'content': 'I am sorry to hear that. Can you provide your order number?'}
]
# Example usage
prompt = chat_template.invoke({'conversation_history': conversation_history, 'query': HumanMessage(content='Where is my refund')}) 

print(prompt)