from fastapi import FastAPI
from app.core.database import init_db

app = FastAPI(title="Messenger API")

# Инициализация базы данных
@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Messenger API is running!"}
