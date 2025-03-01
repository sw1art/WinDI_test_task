from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.models.message import Message
from app.schemas.message import MessageCreate, MessageResponse
from app.services.message_service import send_message, get_chat_messages

router = APIRouter()

@router.post("/", response_model=MessageResponse)
async def send_new_message(message_data: MessageCreate, db: AsyncSession = Depends(get_db)):
    return await send_message(db, message_data)

@router.get("/{chat_id}", response_model=list[MessageResponse])
async def get_messages(chat_id: int, db: AsyncSession = Depends(get_db)):
    return await get_chat_messages(db, chat_id)
