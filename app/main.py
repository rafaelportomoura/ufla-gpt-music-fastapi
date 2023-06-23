from os import sep

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.music import Music

app = FastAPI()

APP_DIR = sep.join(__file__.split(sep)[0:-1])
STATIC_DIR = APP_DIR + sep + "static"

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static/html")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/music", response_class=JSONResponse)
async def get_musics(q: str) -> JSONResponse:
    m = Music()
    return m.get_musics(m)
