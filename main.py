from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {'response': {'message': 'Hellow world.'}}

@app.get("/blog/{id}")
async def blog_posts(id:int):
    return {'data': id}


@app.get("/blog/{id}/comments")
async def blog_comments(id:int):
    return {'post': id, 'comments': f'comments of {id}'}