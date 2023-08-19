from fastapi import FastAPI, HTTPException, Depends, status
from typing import Optional, Annotated
from pydantic import BaseModel;
app = FastAPI()

students = {
    1:{
        "name" : "nehal",
        "age" : 21,
        "year" : "BE-CSE"
    },
    2:{
        "name" : "fahad",
        "age" : 20,
        "year" : "BS-CS"
    }    
}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/")
def home():
    return {"name" : " Hello world "}

# Path Parameter
# GET student_id from user as a parameter
@app.get("/get_student/{student_id}")
def get_students(student_id: int):
    return students[student_id]

# Query Parameter along Path Parameter
@app.get("/get-by-name-id/{id}")
def get_std(*, id: int, name: Optional[str] = None, age: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
            
    return {"message":"Data not found"}

@app.post("/create_students/{student_id}")
def create_students(student_id: int, student: Student):
    if student_id in students:    #if student_id exists in student Object
        return {"Error" : "Student already exists"}
    
    students[student_id] = student
    return students[student_id]