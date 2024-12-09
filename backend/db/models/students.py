
from sqlalchemy import String, Integer, Column, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from db.base_class import Base


class Students(Base):
    __tablename__ = "students"
    id = Column(Integer)
    student_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    address = Column(String, nullable=True)
    phone = Column(Integer, nullable=True)
    student_level = Column(Integer, nullable=False)
#    course_code = Column(Integer, ForeignKey("course_code"))
#    course = relationship("Course", back_populates="student")
    is_active = Column(Boolean, default=True)
