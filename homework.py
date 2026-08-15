from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Classifier(BaseModel):
  age : int
  degree : str
  cpi : int
  color : int

@app.post("/")

def JobClassifier(application: Classifier):
  if application.age < 22 and application.degree == "btech" and application.cpi > 8 and application.color == 1 :
    decision = "approved"
  else:
    decision = "rejected"

  return {
    "Decision" : decision
  }