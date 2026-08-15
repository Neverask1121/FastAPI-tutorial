from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
  age : int
  income : float
  employee_experiece : int

@app.post("/postfunc")

def LoanApplicationModel(application: LoanApplication):
  if application.age < 18 and application.income > 11 and application.employee_experiece < 2:
    decision = "rejected"
  else : 
    decision = "approved"

  return{
    "Age of the applcant" : application.age,
    "DECISION" : decision
  }