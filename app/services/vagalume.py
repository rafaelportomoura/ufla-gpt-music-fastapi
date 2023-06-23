import requests
import re
from services.webscraping import extrair_link_capa


class VagalumeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Vagalume:
    def __init__(self) -> None:
        self.API = "https://api.vagalume.com.br"
        self.SITE = "https://vagalume.com.br"
        self.SEARCH = f"{self.API}/search"
        self.SEARCH_MUS = f"{self.SEARCH}.excerpt"

    def get_art_mus(self, query: str) -> dict | None:
        parametros = {"q": query, "limit": 1}

        response = requests.get(self.SEARCH_MUS, params=parametros)

        if response.status_code == 200:
            docs = response.json()["response"]["docs"]

            if len(docs) == 0:
                data = {
                    "vagalume": "",
                    "capa": "",
                    "Artist": "NotFound",
                    "Band": "NotFound",
                }
                return data

            data = docs[0]

            data["vagalume"] = f"{self.SITE}{data['url']}"
            capa = extrair_link_capa(data["vagalume"])

            regex = re.compile(r"^\/|^[^h]")
            data["capa"] = f"{self.SITE}{capa}" if regex.match(capa) else capa

            return data
        else:
            raise VagalumeError(
                "Erro na requisição da api de art mus:", response.status_code
            )
