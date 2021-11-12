from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session
from . import schemas, models
from .BlogDB import engine, SessionLocal


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.post("/blog")
async def create(request: schemas.Blog, db:Session = Depends(get_db)):
    new_post = models.Blog(post_title=request.post_title, post_body=request.post_body)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post