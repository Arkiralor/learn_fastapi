from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
    user_name: str
    user_email: str
    user_password: str


class ShowUser(BaseModel):
    user_name: str
    user_email: str

    class Config():
        orm_mode = True


class ShowAuthor(BaseModel):
    user_name: str

    class Config():
        orm_mode = True


class Blog(BaseModel):
    post_title: str
    post_body: str

    class Config():
        orm_mode = True

class UpdateBlog(BaseModel):
    post_title: Optional[str] = None
    post_body: Optional[str] = None

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    post_title: str
    post_body: str
    author: ShowAuthor

    class Config():
        orm_mode = True


class ShowAllPosts(BaseModel):
    user_name: str
    user_email: str
    posts: List[Blog] = []

    class Config():
        orm_mode = True

class Login(BaseModel):
    user_email: str
    user_password: str
    
    class Config():
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_email: Optional[str] = None

class ShowUser(BaseModel):
    user_id: int
    user_name: str
    user_email: str

    class Config():
        orm_mode = True
