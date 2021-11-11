from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


app = FastAPI()

@app.post("/blog")
async def create(request: Blog):
    return {'response': f'Blog post {request.title} created.'}