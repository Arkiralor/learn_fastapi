'''
Custom Functions:
'''
from .BlogDB import SessionLocal
from passlib.context import CryptContext




def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")





