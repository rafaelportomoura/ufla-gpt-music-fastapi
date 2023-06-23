from json import dumps
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.music import Music


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static/html")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/music")
async def get_musics(q: str = None):
    m = Music()
    musics = m.get_musics(q)
    return dumps(musics)
