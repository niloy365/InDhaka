from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "InDhaka API is running"}