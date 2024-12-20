from sqlalchemy.orm import Session
from schemas.users import UserCreate
from core.hashing import Hasher
from db.models.users import Users

def create_new_users(users: UserCreate, db: Session):
    users = Users(
    #    fname = students.first_name,
    #    lname = students.last_name,
        email = users.email,
        password = Hasher.get_password_hash(users.password),
    #    student_level = students.student_level,
    #    phone = students.phone,
    #    address = students.address
    )
    db.add(users)
    db.commit()
    db.refresh(users)
    return users