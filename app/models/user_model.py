from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from app.core.db import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    balance = Column(Integer, default=0)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text("now()"))