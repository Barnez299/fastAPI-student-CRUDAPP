from fastapi import FastAPI, Depends
from config import engine
from config import metadata, database

import uvicorn

from sql_app.route import post_route

metadata.create_all(engine)


app = FastAPI(
              title="FastAPI CRUD Example",
              docs_url="/docs", redoc_url="/redocs"
)


''' APP EVENT SETTING'''
@app.on_event("startup")
async def startup():
     await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(post_route, prefix="/api/student", tags=["student"])


@app.get("/")
def home():
    return {"message": "Welcome to FastAPI CRUD Example."}




if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000)