from app.core.db import Base, engine 
from app.models.user import User 

print("Creating table....")
Base.metadata.create_all(bind=engine)
print("Table created successfully!")