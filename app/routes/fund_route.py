from fastapi import APIRouter, Depends, HTTPException, status
from app.core.db import get_db
from sqlalchemy.orm import Session
from app.core.oauth2 import get_current_user
from app.schemas import user_schema

router = APIRouter(
    tags=['Fund'] 
)

@router.post('/fund')
def fund_account(payload: user_schema.FundAccount, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    
    amt = payload.amount

    if not isinstance(amt, int) or amt <= 0:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid amount")

    balance = current_user.balance
    current_user.balance = balance + amt
    db.commit()
    db.refresh(current_user)
    return current_user     

