'''
Import Block:
'''
from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session
from . import schemas, models
from .BlogDB import engine, SessionLocal

'''
Argument Declarations:
'''
app = FastAPI()
models.Base.metadata.create_all(bind=engine)


'''
Custom Functions:
'''
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()



'''
API Views:
'''
@app.post("/blog")
async def create(request: schemas.Blog, db:Session = Depends(get_db)):
    new_post = models.Blog(post_title=request.post_title, post_body=request.post_body)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/blog")
async def view(db:Session = Depends(get_db)):
    all_posts = db.query(models.Blog).all()

    return {'blog_posts':all_posts}


@app.get("/blog/{pid:int}")
async def view_blog(pid, db:Session = Depends(get_db)):
    blog_post = db.query(models.Blog).filter(models.Blog.post_id == pid).first()

    return blog_post