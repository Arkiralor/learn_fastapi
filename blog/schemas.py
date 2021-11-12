from pydantic import BaseModel

class Blog(BaseModel):
    post_title:str
    post_body:str