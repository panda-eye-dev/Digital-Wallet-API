from app.core.db import Base, engine 
from app.models.user_model import User
from app.models.transaction_model import Transaction

Base.metadata.create_all(bind=engine)
print("Table created successfully!")