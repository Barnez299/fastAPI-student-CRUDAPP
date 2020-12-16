from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from config import engine
from config import metadata, database
import uvicorn

from sql_app.route import post_route

metadata.create_all(engine)

app = FastAPI()


''' APP EVENT SETTING'''
@app.on_event("startup")
async def startup():
     await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(post_route, prefix="/api/student", tags=["student"])

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        })




if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000)