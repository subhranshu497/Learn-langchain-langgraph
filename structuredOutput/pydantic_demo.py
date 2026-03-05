from pydantic import BaseModel, EmailStr as email, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Subh"
    age: Optional[int] = None
    email: email 
    cgpa: float = Field(gt=0.0, lt=4.0, default=5.0, description="Cumulative Grade Point Average") #gt means greater than and lt means less than

new_student = {"name": "Subh", "age": '37', "email": "subh@example.com", "cgpa": 1.2} #type coersing
student = Student(**new_student)
student_json = student.model_dump_json
print(student_json)