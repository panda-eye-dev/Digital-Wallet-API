from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.db import get_db
from app.core.oauth2 import get_current_user
from app.schemas.user_schema import Pay, PayResponse
from app.models.user_model import User
from app.models.transaction_model import Transaction

router= APIRouter(
    tags=['Send Money']
)

@router.post('/pay', response_model=PayResponse)
def pay(user: Pay, db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    
    send_to_username = user.username 
    amt = user.amount 

    if not isinstance(send_to_username, str) or not isinstance(amt, int) or amt <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid details")
    
    if current_user.username == send_to_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="You cannot pay yourself")
    
    reciever = db.query(User).filter(User.username == send_to_username).first()

    if not reciever:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Recipient does not exist")

    if current_user.balance < amt:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Insufficient balance")
    
    current_user.balance -= amt 
    reciever.balance += amt 

    sender_txn = Transaction(
        user_id = current_user.id,
        kind="debit",
        amount=amt,
        updated_balance=current_user.balance
    )

    reciever_txn = Transaction(
        user_id = reciever.id,
        kind="credit",
        amount=amt,
        updated_balance=reciever.balance
    )

    db.add_all([sender_txn, reciever_txn])
    db.commit()
    db.refresh(current_user)

    return current_user