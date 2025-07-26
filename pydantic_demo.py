from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str = "Khurram"
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0,lt=4,default=2.5,description="A decimal value representing cgpa of the student")

new_student = {"age":"25","email":"abc@gamil.com"}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict)

student_json = student.model_dump_json()