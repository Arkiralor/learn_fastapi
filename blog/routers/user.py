from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from starlette.responses import Response
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models
from fastapi.params import Depends
from ..utils import get_db
from ..hashing import Hashing


router = APIRouter(
    prefix='/user',
    tags= ['User']
)

# Create new User
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
async def create_user(request: schemas.User, db: Session = Depends(get_db)):

    new_user = models.User(user_name=request.user_name,
                           user_email=request.user_email,
                           user_password=Hashing.bcrypt(password=request.user_password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# View list of all Users
@router.get("/all", status_code=status.HTTP_302_FOUND, response_model=List[schemas.ShowUser])
async def show_users(db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()

    if not all_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No users found; kindly add some and try again.')

    return all_users


# Search for user via user_id
@router.get("/{u_id:int}", status_code=status.HTTP_302_FOUND, response_model=schemas.ShowAllPosts)
async def find_user(u_id, response: Response, db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter(
        models.User.user_id == u_id).first()

    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id={u_id}, not found.')

    return found_user


# Search for user via user_name
@router.get("/find_username={u_name:str}", status_code=status.HTTP_302_FOUND, response_model=schemas.ShowUser)
async def find_user(u_name, db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter(
        models.User.user_name == u_name).first()

    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username = {u_name}, not found.')

    return found_user


# Search for user via user_email
@router.get("/search_email={u_email:str}", status_code=status.HTTP_302_FOUND, response_model=schemas.ShowUser)
async def find_user(u_email, response: Response, db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter(
        models.User.user_email == u_email).first()

    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with email = {u_email}, not found.')

    return found_user