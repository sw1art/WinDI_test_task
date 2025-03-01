from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate

async def get_user_by_id(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

async def create_user(db: AsyncSession, user_data: UserCreate):
    new_user = User(**user_data.model_dump()) 
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user
