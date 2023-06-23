from typing import List
from os import environ

KEY = environ["CHATGPT_API_KEY"] if "CHATGPT_API_KEY" in environ else ""


class Gpt:
    def __init__(self, key: str = KEY) -> None:
        self.key = key

    def suggestions(self, query: str) -> List[str]:
        return ["Vamos Fugir", "Saudosa Maloca", query]
