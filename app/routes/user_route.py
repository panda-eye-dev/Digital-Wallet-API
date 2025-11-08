from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import user_schema
from app.core.db import get_db
from app.core import utils
from app.models.user_model import User

router = APIRouter(
    tags=['Register']
)

@router.post('/', response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    existing_username = db.query(User).filter(User.username == user.username).first()
    existing_email = db.query(User).filter(User.email == user.email).first()
    
    if existing_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Username already exists")
    
    if existing_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Email already exists")
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = User(**user.model_dump(exclude_unset=True))
    print(new_user.balance)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

