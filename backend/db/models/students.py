from db.base_class import Base
from pydantic_core.core_schema import nullable_schema
from sqlalchemy import String, Integer, Text, Column, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
#from datetime import datetime, Datetime


class Students(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, index=True)
    password = Column(String, nullable=False)
    student_level = Column(Integer, nullable=False)
    phone = Column(Integer, nullable=True)
    address = Column(String, nullable=False)
    course = relationship("Course", back_populates="student")

