from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.core.oauth2 import get_current_user
from app.schemas import user_schema

router = APIRouter(
    tags=["Balance Check"]
)

@router.get("/balance", response_model=user_schema.BalanceResponse)
def check_balance(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    print(current_user)
    return current_user


