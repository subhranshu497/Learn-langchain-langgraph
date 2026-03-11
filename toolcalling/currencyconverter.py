from langchain_ollama import ChatOllama
from langchain_core.tools import tool, InjectedToolArg
from langchain_core.messages import HumanMessage
import requests
from typing import Annotated
import json

#create a currentcy conversion tool which can take a prompt from user and give the result
# convert 10 USD to INR
# the ans would be 10 USD is 900 INR
#to achieve this i need to create two tools
#get the today's exchange rate
#multiply the exchange rate with the provided value

#create the tool to get the latest exchange rate
#https://v6.exchangerate-api.com/v6/7cc81a8869b057efcb00e23e/latest/USD

@tool
def get_conversion_rate(base_currency: str, target_currency: str)-> float:
    """This function fetches the currency conversion factor between a given base currency and a target currency"""
    url = f'https://v6.exchangerate-api.com/v6/7cc81a8869b057efcb00e23e/pair/{base_currency}/{target_currency}'

    response = requests.get(url)

    return response.json()
#testing of first tool
#con_rate = get_conversion_rate.invoke({'base_currency':'USD','target_currency':'INR'})
#print(con_rate)

@tool
def convert(base_currency: int, conversion_rate: Annotated[float, InjectedToolArg])-> float:
    """based on the injected conversion rate it will calculate the result for the target currency"""
    return base_currency*conversion_rate

#testing of second tool
#target_amt = convert.invoke({'base_currency':10, 'conversion_rate':92.03})

#print(target_amt)

llm = ChatOllama(model="gemma3:4b", temperature=0)

#binding with the tools

llm_with_tools = llm.bind_tools([get_conversion_rate,convert])

messages = [HumanMessage('What is the conversion rate between INR and USD, and based on the exchange rate calculate 10 INR to usd')]

ai_msg = llm_with_tools.invoke(messages)
messages.append(ai_msg)

for tool_call in ai_msg.tool_calls:
    #execute the first tool and get the conversion rate
    if tool_call['name'] == 'get_conversion_rate':
        tool_msg1 = get_conversion_rate.invoke(tool_call)
        #get the conversion rate
        conv_rate = json.loads(tool_msg1.content)['conversion_rate']
        #append this msg to the msg list
        messages.append(tool_msg1)

    #ex the second tool
    if tool_call['name'] == 'convert':
        #fetch the curr arg
        tool_call['args']['conversion_rate'] = conv_rate
        tool_msg2 = convert.invoke(tool_call)
        messages.append(tool_msg2)

res = llm_with_tools.invoke(messages).content
print(res)