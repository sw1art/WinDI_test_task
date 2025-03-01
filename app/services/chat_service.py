from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.chat import Chat
from app.schemas.chat import ChatCreate
from app.models.group import Group  # Импортируем модель для работы с группами

async def create_chat(db: AsyncSession, chat_data: ChatCreate):
    chat_dict = chat_data.model_dump()
    chat_dict.pop("is_group", None)
    new_chat = Chat(**chat_dict)
    db.add(new_chat)
    await db.commit()   
    await db.refresh(new_chat)
    return new_chat

async def get_chat_by_id(db: AsyncSession, chat_id: int):
    result = await db.execute(select(Chat).filter(Chat.id == chat_id))
    return result.scalars().first()

async def add_user_to_group(db: AsyncSession, group_id: int, user_id: int):
    result = await db.execute(select(Group).filter(Group.id == group_id))
    group = result.scalars().first()

    if group:
        group.members.append(user_id)  
        await db.commit()
        return group
    return None

async def get_user_chats(db: AsyncSession, user_id: int):
    result = await db.execute(select(Chat).filter(Chat.members.contains(user_id)))
    return result.scalars().all()
