from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
  return {"message", "Hello bro how are you I am fine thank you"}

