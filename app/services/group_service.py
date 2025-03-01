from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException

from app.models.group import Group
from app.models.user import User
from app.schemas.group import GroupCreate

async def create_group_service(db: AsyncSession, group_data: GroupCreate):
    new_group = Group(name=group_data.name, creator_id=group_data.creator_id)
    db.add(new_group)  
    await db.commit()
    await db.refresh(new_group, ["users"])
    return new_group

async def add_user_to_group_service(db: AsyncSession, group_id: int, user_id: int):
    result = await db.execute(select(Group).filter(Group.id == group_id))
    group = result.scalars().first()

    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalars().first()

    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    await db.refresh(group, ["users"])

    if user in group.users:
        raise HTTPException(status_code=400, detail="User already in group")

    group.users.append(user)
    await db.commit()
    await db.refresh(group)

    return {"message": "User added to group"}
