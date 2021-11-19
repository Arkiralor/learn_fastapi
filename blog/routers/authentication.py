from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from starlette import status
from ..utils import get_db
from ..hashing import Hashing
from .. import schemas, models

router = APIRouter(
    tags=['Authentication']
)

@router.post("/login")
async def user_login(request: schemas.Login, db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter(models.User.user_email == request.user_email).first()
    
    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No one with {request.user_email} found; kindly check.')

    if not (Hashing.bcrypt(request.user_password) == found_user.user_password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Password incorrect; please check if CapsLock is turned on.')

    # TODO: Generate JWT token and return it

    return found_user