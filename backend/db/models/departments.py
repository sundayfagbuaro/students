from db.base_class import Base
from pydantic_core.core_schema import nullable_schema
from sqlalchemy import String, Integer, Text, Column, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
#from datetime import datetime, Datetime


class Departments(Base):
    __tablename__ = 'departments'
    id = Column(Integer,index=True)
    dept_name = Column(String)
    dept_code = Column(String, primary_key=True, nullable=False)
#    students = Column(Integer, ForeignKey("students.student_id"))
    course_code = Column(String, ForeignKey("courses.course_code"))
#    student = relationship("Course", back_populates="taker")
