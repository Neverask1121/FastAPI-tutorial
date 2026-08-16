from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Dataset(BaseModel):
  name : str
  salary : float
  risk : str
  gender : str

@app.post("/dieforyou")

def InsurancePredictor(application : Dataset):
  approved = (
    application.salary < 1000000 and
    application.risk == "low" and
    application.gender == "Female"
  )
  return {
    "Application status" : "approved" if approved else "rejected",
    "Name" : application.name,
    "Salary" : application.salary,
    "risk" : application.risk,
    "gender" : application.gender
  }