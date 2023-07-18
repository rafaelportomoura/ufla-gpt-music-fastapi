import requests
from typing import List
from os import environ

KEY = environ["CHATGPT_API_KEY"] if "CHATGPT_API_KEY" in environ else ""


class Gpt:
    def __init__(self, key: str = KEY) -> None:
        self.key = key
        self.url = 'https://api.openai.com/v1/chat/completions'
        self.headers = {"Authorization": f"Bearer {self.key}"}

    def suggestions(self, query: str) -> List[str]:
        params = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": query}],
        }
        response = requests.post(self.url, json=params, headers=self.headers)
        result_list = []
        print(response.json())

        if(response.status_code == 200):
            result_list = response.json()["choices"][0]["message"]["content"].split(';');

        return result_list
