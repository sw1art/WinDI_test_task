from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.database import init_db
from app.api.routers import ws_chat, user, chat, message, group

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="Messenger API", lifespan=lifespan)

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(chat.router, prefix="/chats", tags=["Chats"])
app.include_router(ws_chat.router)
app.include_router(message.router, prefix="/messages", tags=["Messages"])
app.include_router(group.router, prefix="/groups", tags=["Groups"])

@app.get("/")
async def root():
    return {"message": "Messenger API is running!"}