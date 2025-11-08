from fastapi import APIRouter, Depends
from app.core.db import get_db
from app.core.oauth2 import get_current_user
from sqlalchemy.orm import Session
from app.models.transaction_model import Transaction

router = APIRouter(
    tags=['Statement']
)

@router.get('/statement')
def get_statement(db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    transactions = db.query(Transaction).filter(Transaction.user_id ==  current_user.id).order_by(Transaction.created_at.desc()).all()

    return transactions

