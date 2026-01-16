# from typing import Annotated
# from datetime import datetime,timedelta , timezone 
# from fastapi import FastApi , depends , HTTPException, Query
#from sqlmodel import Field, Session, SQLModel, create_engine, select
from fastapi import FastAPI
from db.database import create_db_and_tables
from routes import user

app = FastAPI()



@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(user.router)