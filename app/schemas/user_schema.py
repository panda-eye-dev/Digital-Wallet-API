from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    balance: Optional[int] = None

    class Config:
        from_attributes: True

class UserResponse(BaseModel):
    username: str 
    email: EmailStr
    balance: int
    created_at: datetime

class UserLogin(BaseModel):
    username: str 
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    id: int
    username: str 
    email: EmailStr
    balance: int

class Token(BaseModel):
    access_token: str 
    token_type: str 

class TokenData(BaseModel):
    id: Optional[int] = None

class FundAccount(BaseModel):
    amount: int 

class FundResponse(BaseModel):
    id: int
    username: str 
    balance: int

class BalanceResponse(BaseModel):
    balance: int

class Pay(BaseModel):
    username: str 
    amount: int 

class PayResponse(BaseModel):
    username: str 
    balance: int

    class Config:
        from_attributes: True