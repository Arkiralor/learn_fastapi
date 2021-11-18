from passlib.context import CryptContext

# Variable Declarations:
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hashing():    
    def bcrypt(password: str):
        
        return pwd_context.hash(password)