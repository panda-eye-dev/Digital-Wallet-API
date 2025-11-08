from fastapi import FastAPI, Depends
from app.core.db import get_db
import app.__init__db
from app.routes import user_route, auth_route, fund_route, balance, transaction_route, pay

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello world!"}

app.include_router(user_route.router)
app.include_router(auth_route.router)
app.include_router(fund_route.router)
app.include_router(balance.router)
app.include_router(transaction_route.router)
app.include_router(pay.router)




