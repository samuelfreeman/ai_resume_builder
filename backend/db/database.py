from sqlmodel import SQLModel, Session  ,create_engine 
from app.config.config import DATABASE_URL

engine = create_engine(DATABASE_URL,echo = True)
def create_db_and_table():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session