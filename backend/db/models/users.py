from db.base_class import Base
from pydantic_core.core_schema import nullable_schema
from sqlalchemy import String, Integer, Text, Column, Boolean, ForeignKey, Index
from sqlalchemy.orm import relationship
#from datetime import datetime, Datetime


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,index=True)
    full_name = Column(String)
#    last_name = Column(String,nullable=False)
    email = Column(String, unique=True,nullable=False,index=True)
    password = Column(String,nullable=False)
    is_active = Column(Boolean, default=True)
    is_student = Column(Boolean, default=True)
    is_tutor = Column(Boolean, default=False)
    student_level = Column(Integer)
#    phone = Column(Integer,nullable=True)
#    address = Column(String,nullable=False)
#    student = relationship("Course", back_populates="taker")


