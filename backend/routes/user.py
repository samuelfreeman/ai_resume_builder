from fastapi import APIRouter, Depends, HTTPException, Query
from typing import Annotated
from sqlmodel import Session, select
from datetime import timedelta

from db.database import get_session
from db.models import User
from schemas.user import SignUpRequest, LoginRequest, AuthResponse
from utils.security import create_access_token, verify_password, password_hash
from config.config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(tags=["Users"])

SessionDep = Annotated[Session, Depends(get_session)]

@router.post("/signup", response_model=AuthResponse)
def register_user(user: SignUpRequest, session: SessionDep):
    existing_user = session.exec(
        select(User).where(User.email == user.email)
    ).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")

    db_user = User(
        fullname=user.fullname,
        email=user.email,
        password=password_hash(user.password),
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    token = create_access_token(
        {"sub": str(db_user.id)},
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return UserResponse(
        id=db_user.id,
        fullname=db_user.fullname,
        email=db_user.email,
        access_token=token,
    )
