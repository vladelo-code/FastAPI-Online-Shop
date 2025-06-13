from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta

from ecommerce import db
from ecommerce.user import hashing
from ecommerce.user.models import User
from ecommerce.auth import jwt

router = APIRouter(tags=['Authentication'])


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), database: Session = Depends(db.get_db)):
    user = database.query(User).filter(User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found!")

    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password!")

    # Generate JWT token
    access_token = jwt.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
