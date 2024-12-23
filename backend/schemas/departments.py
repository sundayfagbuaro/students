from pydantic import BaseModel, EmailStr, Field


class DepartmentCreate(BaseModel):
    dept_name: str
    dept_code: str = Field(..., min_length=3, max_length=3)


class ShowDepartments(BaseModel):
    dept_name: str
    dept_code: str

    class Config:
        orm_mode = True