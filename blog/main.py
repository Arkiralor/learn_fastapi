from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.post("/")
async def root ():
    return {'message': 'Hello world!'}