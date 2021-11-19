from pydantic import BaseModel
from typing import List


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
