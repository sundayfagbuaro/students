from fastapi import APIRouter
from apis.v1 import route_users
from apis.v1 import route_departments
from apis.v1 import route_courses

api_router = APIRouter()

api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_departments.router, prefix="/departments", tags=["departments"])
api_router.include_router(route_courses.router, prefix="/courses", tags=["courses"])