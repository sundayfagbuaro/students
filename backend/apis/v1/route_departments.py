from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.departments import DepartmentCreate
from db.session import get_db

from db.crud.departments import create_new_departments
from schemas.departments import ShowDepartments
from fastapi import status


router = APIRouter()


@router.post('/', response_model=ShowDepartments, status_code=status.HTTP_201_CREATED)
def create_department(departments: DepartmentCreate, db: Session = Depends(get_db)):
    departments = create_new_departments(departments=departments, db=db)
    return departments