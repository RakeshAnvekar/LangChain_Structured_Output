from pydantic import BaseModel, Field

from dotenv import load_dotenv
load_dotenv()

class Student(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="The name of the student",default="Unknown")
    age: int = Field(gt=10, le=10, description="The age of the student")
    cgpa: float = Field(gt=0.0, le=4.0, description="The CGPA of the student")

student={
        "name": "John Doe",
        "age": 9,
        "cgpa": -3.5
}

student_obj = Student(**student)
print(student_obj)

#you can conert to dictionary of json

print(dict(student_obj)) # Pydentic to dictionary
print(student_obj.json()) # Pydentic to json