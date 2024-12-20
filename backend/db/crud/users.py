from sqlalchemy.orm import Session
from schemas.users import UserCreate
from core.hashing import Hasher
from db.models.users import Users

def create_new_users(users: UserCreate, db: Session):
    users = Users(
        first_name = users.first_name,
        last_name = users.last_name,
        email = users.email,
        password = Hasher.get_password_hash(users.password),
        student_level = users.student_level
    )
    db.add(users)
    db.commit()
    db.refresh(users)
    return users