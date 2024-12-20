from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    first_name: str = Field(max_length=10)
    last_name: str = Field(max_length=20)
    email: EmailStr
    password: str = Field(..., min_length=5, max_length=15)
    student_level: int


class ShowUsers(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    is_student: bool
    student_level: int

    class Config:
        orm_mode = True