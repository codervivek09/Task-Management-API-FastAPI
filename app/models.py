from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(100),unique=True)
    email = Column(String(100),unique=True)
    password = Column(String(255))

    tasks = relationship("Task",back_populates="owner")


class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(200))
    description = Column(String(500))
    status = Column(String(50),default="Pending")

    owner_id = Column(Integer,ForeignKey("users.id"))

    owner = relationship("User",back_populates="tasks")