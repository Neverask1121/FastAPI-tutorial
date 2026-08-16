from fastapi import FastAPI

app = FastAPI()

customer_risk_level = [
  {"name" : "Aditya", "city" :"bangalore", "risk" : "high"},
  {"name" : "Aditya", "city" :"mangalore", "risk" : "low"},
  {"name" : "Aditya", "city" :"jangalore", "risk" : "low"},
  {"name" : "Aditya", "city" :"langalore", "risk" : "low"},
  {"name" : "Aditya", "city" :"kangalore", "risk" : "low"},
  {"name" : "Aditya", "city" :"uangalore", "risk" : "high"},
]

@app.get("/customer")

def testing_query(city : str, risk : str):
  
  