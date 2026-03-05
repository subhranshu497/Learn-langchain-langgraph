from langchain_core.prompts import ChatPromptTemplate

# Define a chat prompt template
chat_template = ChatPromptTemplate(
    [
        ('system', 'You are a helpful {domain} expert.'),
        ('human', 'Tell me about {topic}.')
    ]
)
# Example usage
prompt = chat_template.invoke({'domain': 'technology', 'topic': 'LangChain'})
print(prompt)
