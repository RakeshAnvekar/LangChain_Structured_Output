from pydantic import BaseModel

from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None


    #create the dictionary
new_student ={
    "name": "Rakesh",
    "age": "trrr"
}
stdent= Student(**new_student)
print(stdent.name)  # Output: Rakesh
print(stdent.age)  # Output: None