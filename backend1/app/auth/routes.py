from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.auth.schemas import UserCreate, Token
from app.auth.service import create_user, authenticate_user
from app.core.security import create_access_token

router = APIRouter()

@router.post("/register")
async def register(data: UserCreate, db: AsyncSession = Depends(get_db)):
    await create_user(db, data.email, data.password)
    return {"message": "User created"}

@router.post("/login", response_model=Token)
async def login(data: UserCreate, db: AsyncSession = Depends(get_db)):
    user = await authenticate_user(db, data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.id})
    return {"access_token": token, "token_type": "bearer"}
