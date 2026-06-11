from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate, UserLogin
from app.auth import hash_password, verify_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Register
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    new_user = User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()

    return {"message": "User Registered"}


# Login
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User)\
                .filter(User.email == user.email)\
                .first()

    if not db_user:
        return {"message": "Invalid Email"}

    if not verify_password(user.password, db_user.password):
        return {"message": "Invalid Password"}

    return {"message": "Login Successful"}