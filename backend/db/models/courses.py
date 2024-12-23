from pydantic_core.core_schema import nullable_schema
from sqlalchemy import String, Integer, Text, Column, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
#from datetime import datetime, Datetime
from db.base_class import Base


class Courses(Base):
    __tablename__ = 'courses'
    id = Column(Integer,index=True)
    course_name = Column(String)
    course_code = Column(String, primary_key=True, nullable=False)
#    students = Column(Integer, ForeignKey("students.student_id"))
    department = Column(String, ForeignKey("departments.dept_code"))
#    student = relationship("Course", back_populates="taker")