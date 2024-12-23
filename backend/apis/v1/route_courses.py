from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.courses import CourseCreate
from db.session import get_db

from db.crud.courses import create_new_courses
from schemas.courses import ShowCourses
from fastapi import status


router = APIRouter()


@router.post('/', response_model=ShowCourses, status_code=status.HTTP_201_CREATED)
def create_course(courses: CourseCreate, db: Session = Depends(get_db)):
    courses = create_new_courses(courses=courses, db=db)
    return courses