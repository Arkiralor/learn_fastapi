from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
from starlette.responses import Response
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models
from fastapi.params import Depends
from ..utils import get_db


router = APIRouter()

# Add blog post to DB
@router.post("/blog", status_code=status.HTTP_201_CREATED, tags=['blog_posts'])
async def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_post = models.Blog(post_title=request.post_title,
                           post_body=request.post_body,
                           author_id=1)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# Delete blog post in DB via Post_ID
@router.delete("/blog/delete/{pid:int}", status_code=status.HTTP_204_NO_CONTENT, tags=['blog_posts'])
async def destroy(pid, db: Session = Depends(get_db)):
    try:
        db.query(models.Blog).filter(models.Blog.post_id ==
                                     pid).delete(synchronize_session=False)
        db.commit()
        return {'response': f'Blog post with id= {pid} was successfully deleted.'}

    except Exception as e:
        return {'Error': f'{e}. Blog post with id= {pid} does not exist.'}


# Update blog post in DB via Post_ID
@router.put("/blog/update/{pid:int}", status_code=status.HTTP_202_ACCEPTED, tags=['blog_posts'])
async def update(pid, request: schemas.Blog, db: Session = Depends(get_db)):
    pass


# Get all blog posts from DB
@router.get("/blog", status_code=status.HTTP_202_ACCEPTED, response_model=List[schemas.ShowBlog], tags=['blog_posts'])
async def view_all_posts(db: Session = Depends(get_db)):
    all_posts = db.query(models.Blog).all()

    return all_posts


# Search for a blog post via Post_ID
@router.get("/blog/{pid:int}", status_code=status.HTTP_302_FOUND, response_model=schemas.ShowBlog, tags=['blog_posts'])
async def view_blog(pid, response: Response, db: Session = Depends(get_db)):
    blog_post = db.query(models.Blog).filter(
        models.Blog.post_id == pid).first()

    if not blog_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog post with id={pid}, not found.')

    return blog_post
