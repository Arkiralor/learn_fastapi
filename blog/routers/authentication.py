from datetime import timedelta
from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status
from ..utils import get_db
from ..hashing import Hashing
from .. import models
from ..JWToken import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token

router = APIRouter(
    tags=['Authentication']
)


@router.post("/login")
async def user_login(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter(
        models.User.user_email == request.username).first()

    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No one with {request.username} found; kindly check.')

    if not Hashing.verify(found_user.user_password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Password incorrect; please check if CapsLock is turned on.')

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": found_user.user_email},
        expires_delta=access_token_expires
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
