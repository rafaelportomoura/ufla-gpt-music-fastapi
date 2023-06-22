import requests
from webscraping import extrair_link_capa


class VagalumeError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Vagalume:
    def __init__(self) -> None:
        self.API = "https://api.vagalume.com.br"
        self.SITE = "https://vagalume.com.br"
        self.SEARCH = f"{self.API}/search"
        self.SEARCH_ARTMUS = f"{self.SEARCH}.artmus"

    def get_art_mus(self, query: str) -> dict | None:
        parametros = {"q": query, "limit": 1}

        response = requests.get(self.SEARCH_ARTMUS, params=parametros)

        if response.status_code == 200:
            data = response.json()["response"]["docs"][0]

            data["vagalume"] = f"{self.SITE}{data['url']}"
            data["capa"] = extrair_link_capa(data["vagalume"])

            return data
        else:
            raise VagalumeError(
                "Erro na requisição da api de art mus:", response.status_code
            )
