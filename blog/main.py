from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import Response
from typing import List
from . import schemas, models
from .BlogDB import engine
from .utils import get_db
from .hashing import Hashing


'''
Argument Declarations:
'''
app = FastAPI()
models.Base.metadata.create_all(bind=engine)


'''
API Views:
'''

# Add blog post to DB


@app.post("/blog", status_code=status.HTTP_201_CREATED, tags=['blog_posts', 'create'])
async def create(request: schemas.Blog, db: Session = Depends(get_db)):
    new_post = models.Blog(post_title=request.post_title,
                           post_body=request.post_body)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# Delete blog post in DB via Post_ID
@app.delete("/blog/delete/{pid:int}", status_code=status.HTTP_204_NO_CONTENT, tags=['blog_posts', 'delete'])
async def destroy(pid, db: Session = Depends(get_db)):
    try:
        db.query(models.Blog).filter(models.Blog.post_id ==
                                     pid).delete(synchronize_session=False)
        db.commit()
        return {'response': f'Blog post with id= {pid} was successfully deleted.'}

    except Exception as e:
        return {'Error': f'{e}. Blog post with id= {pid} does not exist.'}


# Update blog post in DB via Post_ID
@app.put("/blog/update/{pid:int}", status_code=status.HTTP_202_ACCEPTED, tags=['blog_posts', 'put'])
async def update(pid, request: schemas.Blog, db: Session = Depends(get_db)):
    pass


# Get all blog posts from DB
@app.get("/blog", status_code=status.HTTP_202_ACCEPTED, response_model=List[schemas.ShowBlog], tags=['blog_posts', 'retrieve'])
async def view(db: Session = Depends(get_db)):
    all_posts = db.query(models.Blog).all()

    return all_posts


# Search for a blog post via Post_ID
@app.get("/blog/{pid:int}", status_code=status.HTTP_302_FOUND, response_model=schemas.ShowBlog, tags=['blog_posts', 'retrieve'])
async def view_blog(pid, response: Response, db: Session = Depends(get_db)):
    blog_post = db.query(models.Blog).filter(
        models.Blog.post_id == pid).first()

    if not blog_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog post with id={pid}, not found.')

    return blog_post


# Create new User
@app.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser, tags=['users', 'create'])
async def create_user(request: schemas.User, db: Session = Depends(get_db)):

    new_user = models.User(user_name=request.user_name,
                           user_email=request.user_email,
                           user_password=Hashing.bcrypt(password=request.user_password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# View list of all Users
@app.get("/user/all", status_code=status.HTTP_302_FOUND, response_model=List[schemas.ShowUser], tags=['users', 'retrieve'])
async def show_users(db: Session = Depends(get_db)):
    all_users = db.query(models.User).all()

    if not all_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No users found; kindly add some and try again.')

    return all_users


# Search for user via user_id
@app.get("/user/{u_id:int}", status_code=status.HTTP_302_FOUND, response_model=schemas.ShowUser, tags=['users', 'retrieve'])
async def find_user(u_id, response: Response, db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter(
        models.User.user_id == u_id).first()

    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id={u_id}, not found.')

    return found_user


# Search for user via user_name
@app.get("/user/find_username={u_name:str}", status_code=status.HTTP_302_FOUND, response_model=schemas.ShowUser, tags=['users', 'retrieve'])
async def find_user(u_name, response: Response, db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter(
        models.User.user_name == u_name).first()

    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with username = {u_name}, not found.')

    return found_user


# Search for user via user_email
@app.get("/user/search_email={u_email:str}", status_code=status.HTTP_302_FOUND, response_model=schemas.ShowUser, tags=['users', 'retrieve'])
async def find_user(u_email, response: Response, db: Session = Depends(get_db)):
    found_user = db.query(models.User).filter(
        models.User.user_email == u_email).first()

    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with email = {u_email}, not found.')

    return found_user
