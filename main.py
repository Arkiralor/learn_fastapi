from typing import Optional
from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
async def index():
    return {'response': {'message': 'Hellow world.'}}


@app.get("/blog")
async def blogs(limit = 10, published:bool = True, sort: Optional[str] = None ):
    if published:
        return {'data': f'{limit} published blogs.'}
    else:
        return {'data': f'List of {limit} blogs.'} 
    



@app.get("/blog/unpublished")
async def unpublished_blogs():
    return {'data': 'Unpublished Blogs'}

@app.get("/blog/{id}")
async def blog_posts(id:int):
    return {'data': id}


@app.get("/blog/{id}/comments")
async def blog_comments(id:int, limit:int =50):

    return {'post': id, f'{limit} comments': f'{limit} comments of post: {id}.'}