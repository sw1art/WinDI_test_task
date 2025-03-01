from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.chat import Chat
from app.schemas.chat import ChatCreate, ChatResponse
from app.services.chat_service import create_chat, get_chat_by_id

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def create_new_chat(chat_data: ChatCreate, db: AsyncSession = Depends(get_db)):
    return await create_chat(db, chat_data)

@router.get("/{chat_id}", response_model=ChatResponse)
async def get_chat(chat_id: int, db: AsyncSession = Depends(get_db)):
    return await get_chat_by_id(db, chat_id)
