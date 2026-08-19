from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {
  "S001":{"name":"Aditya", "marks":90, "grade":"A"},
  "S002":{"name":"Pranjal", "marks":67, "grade":"B"},
  "S003":{"name":"Miya", "marks":69, "grade":"B"},``
  "S004":{"name":"Adrish", "marks":10, "grade":"F"}
}

@app.get("/student/{student_id}")
def get_student(student_id : str):
  if student_id not in students:
    raise HTTPException(
      status_code = 404, 
      detail=f"The id {student_id} doesnot exists in the DB."
    )
  return students[student_id]