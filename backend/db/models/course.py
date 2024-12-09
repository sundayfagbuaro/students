from pydantic_core.core_schema import nullable_schema
from sqlalchemy import String, Integer, Text, Column, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
#from datetime import datetime, Datetime
from db.base_class import Base


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String, nullable=False)
    course_title = Column(String, nullable=False)
    taker_id = Column(Integer, ForeignKey("students.student_id"))
    student = relationship("Student", back_populates="course")