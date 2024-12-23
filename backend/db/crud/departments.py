from sqlalchemy.orm import Session
from schemas.departments import DepartmentCreate
from db.models.departments import Departments


def create_new_departments(departments: DepartmentCreate, db: Session):
    departments = Departments(
        dept_name = departments.dept_name,
        dept_code = departments.dept_code
    )
    db.add(departments)
    db.commit()
    db.refresh(departments)
    return departments