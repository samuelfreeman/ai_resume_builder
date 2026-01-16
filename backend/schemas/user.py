from pydantic import BaseModel
from typing import List, Optional

class SignUpRequest(BaseModel):
    fullname: str
    email:str
    password:str

class LoginRequest(BaseModel):
    email: str
    password:str


class AuthResponse(BaseModel):
    id: str
    fullname: str
    email: str
    access_token: str
    token_type: str = "bearer"
