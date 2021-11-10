from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.post("/blog")
async def create():
    return {'response': 'Blog post created.'}