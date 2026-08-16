from fastapi import FastAPI

app = FastAPI()

customer_risk_level = [
  {"name" : "Aditya", "city" :"bangalore", "risk" : "high"},
  {"name" : "Aditya", "city" :"bangalore", "risk" : "high"},
  {"name" : "Aditya", "city" :"bangalore", "risk" : "high"},
  {"name" : "Aditya", "city" :"bangalore", "risk" : "high"},
]

@app.get("/customer")

def testing_query(city : str, risk : str):
  filtered = [
    c for c in customer_risk_level
    if c["city"] == city and c["risk"] == risk
  ]
  return{
    "No. of memebers found" : len(filtered),
    "city" : city,
    "id" : id,
    "risk" : risk,
    "results" : filtered
  }
  