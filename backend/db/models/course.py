from datetime import datetime
from sqlalchemy import String, Integer, Column, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.base_class import Base


class Course(Base):
    __tablename = "course"
    id = Column(Integer, primary_key=True, index=True)
    course_code = Column(String(6), nullable=False)
    course_title = Column(String(100), nullable=False)
    course_unit = Column(Integer, nullable=False)
    course_tutor = Column(String(25))
    course_outline = Column(Text, nullable=True)
    course_level = Column(Integer, nullable=False)
    course_taker_id = Column(Integer, ForeignKey("student.id"))
    student = relationship("Student", back_populates="course")
    is_active = Column(Boolean, default=True)
