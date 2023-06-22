import re

import requests
from bs4 import BeautifulSoup


class WebScrapingError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def extrair_link_capa(url: str) -> str | None:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code != 200:
        raise WebScrapingError("Erro na requisição de extrair capa:", response.status_code)

    capa = None

    # Encontre a tag <iframe> com um padrão de URL do YouTube
    imagem_capa = soup.find('meta', property='og:image')

    if imagem_capa:
        capa = imagem_capa["content"]

    return capa
