from pydantic import BaseModel, EmailStr, Field


class CourseCreate(BaseModel):
    course_name: str
    course_code: str = Field(..., min_length=6, max_length=6)


class ShowCourses(BaseModel):
    course_name: str
    course_code: str


    class Config:
        orm_mode = True