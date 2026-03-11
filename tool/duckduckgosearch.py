from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke('top news of USA today')

print(result)

## this is an example of Builtin tool