from pydantic import BaseModel, EmailStr

class Student(BaseModel):
    name: str = "Default Name"  
    email: EmailStr            # Validates email format

# Dictionary (simulating input data)
new_student = {
    "name": "Rakesh",
    "email": "abc"
}

# Convert dictionary → validated Pydantic model
student = Student(**new_student)

print(student.name)
print(student.email)
