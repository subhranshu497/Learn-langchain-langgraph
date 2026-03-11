from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class MultiplyInput(BaseModel):
    a: int=Field(required=True, description="The first number to add")
    b: int=Field(required=True, description="The second number to add")

def multiply_fun(a: int, b: int)->int:
    return a*b

multiply_tool = StructuredTool.from_function(
    func=multiply_fun,
    name='multiply',
    description="Multiply Two Numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({'a':4, 'b':5})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)