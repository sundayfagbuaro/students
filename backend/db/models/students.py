
from sqlalchemy import String, Integer, Column, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from db.base_class import Base


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, unique=True)
    email = Column(String(30), nullable=False, unique=True, index=True)
    password = Column(String(20), nullable=False)
    address = Column(String(50), nullable=True)
    phone = Column(Integer, nullable=True)
    student_level = Column(Integer(), nullable=False)
#    course_code = Column(Integer, ForeignKey("course_code"))
    course = relationship("Course", back_populates="student")
    is_active = Column(Boolean, default=True)
