from pydantic import BaseModel


class Blog(BaseModel):
    post_title: str
    post_body: str


class ShowBlog(Blog):
    post_body: str

    class Config():
        orm_mode = True
