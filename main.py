#fast api, uvicorn

from fastapi import FastAPI


app = FastAPI()
@app.get("/")
def greet():
    return "Welcome to Fast API"

