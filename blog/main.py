from fastapi import FastAPI
from . import models
from .BlogDB import engine
from .routers import blog, user


'''
Argument Declarations:
'''
app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(bind=engine)
