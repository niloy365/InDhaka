from fastapi import FastAPI

from .database import Base, engine
from .routes.buses import router as bus_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="InDhaka API")
app.include_router(bus_router)

@app.get("/")
def root():
    return {"message": "InDhaka API is running"}

@app.get("/api/health")
def health():
    return {"status": "ok"}