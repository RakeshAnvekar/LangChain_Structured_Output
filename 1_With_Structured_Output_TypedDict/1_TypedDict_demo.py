from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int
    email: str

new_person: Person = {
    "name": "Alice",
    "age": 30,
    "email": "Alice@gmail.com"
}

print(new_person)
# Output: {'name': 'Alice', 'age': 30, 'email': '