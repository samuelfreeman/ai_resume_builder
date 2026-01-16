from datetime import datetime, timedelta, timezone
import jwt
from pwdlib import PasswordHash
from app.config.config import SECRET_KEY,AlGORITHM

password_hash = PasswordHash.recommended()


def create_access_token(data:dict , expires_delta:timedelta):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+ expires_delta
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=AlGORITHM)


def verify_password(password:str,hashed_password:str )-> bool:
    return password_hash.verify(password, hashed_password)

def hash_password (password:str)-> str:
    return password_hash.hash(password)