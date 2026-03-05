from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    "name": "Subh",
    "age": 37
}
print(new_person)