from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.group import Group
from app.models.user import User
from app.schemas.group import GroupCreate, GroupResponse
from app.services.group_service import create_group_service, add_user_to_group_service

router = APIRouter()

@router.post("/", response_model=GroupResponse)
async def create_group(group_data: GroupCreate, db: Session = Depends(get_db)):
    return await create_group_service(db, group_data)

@router.post("/{group_id}/add_user/{user_id}")
async def add_user_to_group(group_id: int, user_id: int, db: Session = Depends(get_db)):
    return await add_user_to_group_service(db, group_id, user_id)
