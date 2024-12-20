from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users import UserCreate
from db.session import get_db

from db.crud.users import create_new_users
from schemas.users import ShowUsers
from fastapi import status


router = APIRouter()

@router.post('/', response_model=ShowUsers, status_code=status.HTTP_201_CREATED)
def create_user(users: UserCreate, db: Session = Depends(get_db)):
    users = create_new_users(users=users, db=db)
    return users