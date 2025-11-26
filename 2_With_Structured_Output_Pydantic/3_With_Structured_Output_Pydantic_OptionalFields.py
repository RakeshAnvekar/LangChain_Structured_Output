# we have student dictionary , and i want to store student name , i want that student name is only string no oterhter type
from pydantic import BaseModel

class Student(BaseModel):
    name: str="Default Name"


    #create the dictionary
new_student ={
  
}

student= Student(**new_student)
print(student.name)