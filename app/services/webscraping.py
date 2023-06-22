import re

import requests
from bs4 import BeautifulSoup


class WebScrapingError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def extrair_link_youtube(url: str) -> str | None:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code != 200:
        raise WebScrapingError("Erro na requisição de extrair :", response.status_code)

    video_link = None

    # Encontre a tag <iframe> com um padrão de URL do YouTube
    iframe = soup.find("a", src=re.compile(r"(https?://www\.youtube\.com/.*)"))

    if iframe:
        video_link = iframe["src"]

    return video_link
