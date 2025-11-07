from pydantic import BaseModel, EmailStr, SecretStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

