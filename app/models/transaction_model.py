from sqlalchemy import Column, String, Integer, ForeignKey
from app.core.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    kind = Column(String) #"credit"/ "debit"
    amount = Column(Integer, nullable=False)
    updated_balance = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default=text("now()"))

    user = relationship('User', back_populates="transactions")