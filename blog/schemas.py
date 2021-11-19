from pydantic import BaseModel


class Blog(BaseModel):
    post_title: str
    post_body: str


class ShowBlog(BaseModel):
    post_title: str
    post_body: str

    class Config():
        orm_mode = True


class User(BaseModel):
    user_name: str
    user_email: str
    user_password: str


class ShowUser(BaseModel):
    user_name: str
    user_email: str

    class Config():
        orm_mode = True
