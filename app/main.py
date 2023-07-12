from json import dumps
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.music import Music
from fastapi.responses import RedirectResponse


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static/html")


@app.get("/", response_class=RedirectResponse, status_code=302)
async def redirect_home():
    return "/music"


@app.get("/music", response_class=HTMLResponse)
async def read_item(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Music",
            "script": "music",
        },
    )


@app.get("/api/music", response_class=JSONResponse)
async def get_musics(q: str = None) -> str:
    m = Music()
    musics = m.get_musics(q)
    return dumps(musics)
