from fastapi import FastAPI, Depends
from app.schemas import user
from app.models.user import User
from app.core.db import get_db
from sqlalchemy.orm import Session
import app.__init__db
from app.core import utils

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello world!"}

'''
@router.post("/", response_model= schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    #hash the password  - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
'''
@app.post('/')
def create_user(user: user.UserCreate, db: Session = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



