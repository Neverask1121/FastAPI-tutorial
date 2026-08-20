from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {
  "S001":{"name":"Aditya", "marks":90, "grade":"A"},
  "S002":{"name":"Pranjal", "marks":67, "grade":"B"},
  "S003":{"name":"Miya", "marks":69, "grade":"B"},
  "S004":{"name":"Adrish", "marks":10, "grade":"F"}
}

##input schema

class MarksSubmission(BaseModel):
  student_id : str
  name : str
  marks : int
  grade : str


@app.get("/student/{student_id}")
def get_student(student_id : str):
  if student_id not in students:
    raise HTTPException(
      status_code = 404, 
      detail=f"The id {student_id} doesnot exists in the DB."
    )
  return students[student_id]

@app.post("/submit-marks/")
def submitmarks(submission:MarksSubmission):
  #error 1 student doesnot exists
  if submission.student_id not in students:
    raise HTTPException(
      status_code = 404,
      detail=f"The id {submission.student_id} doesnot exists in the database"
    )

  ##error 2 student has entered marks not in range
  if submission.marks < 0 or submission.marks > 100:
    raise HTTPException(
      status_code = 400,
      detail={
        "error":"marks must be in range 0 - 100",
        "marks_received":submission.marks,
        "fix":"enter a value between 0 and 100"
      }
    )
  ##error3 student name is empty
  if submission.grade.strip() == "":
    raise HTTPException(
      status_code = 400,
      detail={
        "Grade name cannot be empty"
      }
    )
  try:
    students[submission.student_id]["marks"] = submission.marks
    return {
      "message":"marks have been submitted successfully",
      "student":students[submission.student_id]["name"],
      "marks":submission.marks
    }
  except Exception as e:
    raise HTTPException(
      status_code = 500,
      detail = f"Something went wrong on this side not your fault bro: {str(e )}"
    )
        
