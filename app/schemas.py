from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username:str
    email:EmailStr
    password:str


class UserLogin(BaseModel):
    email:str
    password:str


class TaskCreate(BaseModel):
    title:str
    description:str



class TaskUpdate(BaseModel):
    title: str
    description: str
    status: str


