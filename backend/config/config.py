import os 
from dotenv import load_dotenv

load_dotenv()



SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("Database url not set")
if not SECRET_KEY:
    raise RuntimeError("Secret key not set")
if not ACCESS_TOKEN_EXPIRE_MINUTES:
    raise RuntimeError("TokenExpiry minutes not set")