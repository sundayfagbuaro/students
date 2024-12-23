from sqlalchemy.orm import Session
from schemas.courses import CourseCreate
from db.models.courses import Courses


def create_new_courses(courses: CourseCreate, db: Session):
    courses = Courses(
        course_name = courses.course_name,
        course_code = courses.course_code
    )
    db.add(courses)
    db.commit()
    db.refresh(courses)
    return courses