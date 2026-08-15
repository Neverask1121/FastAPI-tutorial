from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
  return {"message", "Hello bro how are you I am fine thank you"}

@app.get("/about")
def notabout():
  return {"explaination" : "cricket score predictor model", "Version" : "1.0"}

@app.get("/customer")
def customer(customer_id : int):
  return {
    "customer_id" : customer_id,
    "name" : "Aditya",
    "roll no." : "20252501002"
  }