from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.message import Message
from app.schemas.message import MessageCreate

async def send_message(db: AsyncSession, message_data: MessageCreate):
    new_message = Message(**message_data.model_dump())
    db.add(new_message)
    await db.commit()
    await db.refresh(new_message)
    return new_message

async def get_chat_messages(db: AsyncSession, chat_id: int, limit: int = 50):
    result = await db.execute(
        select(Message).filter(Message.chat_id == chat_id).order_by(Message.timestamp.desc()).limit(limit)
    )
    return result.scalars().all()

async def mark_message_as_read(db: AsyncSession, message_id: int):
    result = await db.execute(select(Message).filter(Message.id == message_id))
    message = result.scalars().first()

    if message:
        message.is_read = True
        await db.commit()
        return message
    return None

async def delete_message(db: AsyncSession, message_id: int):
    """Удаление сообщения."""
    result = await db.execute(select(Message).filter(Message.id == message_id))
    message = result.scalars().first()

    if message:
        await db.delete(message)
        await db.commit()
        return True
    return False
