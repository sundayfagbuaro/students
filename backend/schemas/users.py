from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    full_name: str = Field(max_length=25)
    email: EmailStr
    password: str = Field(..., min_length=5, max_length=15)
    student_level: int


class ShowUsers(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    is_student: bool
    student_level: int

    class Config:
        orm_mode = True