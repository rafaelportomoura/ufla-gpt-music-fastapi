from services.vagalume import Vagalume
from services.gpt import Gpt


class Music:
    def __init__(self, vagalume: Vagalume = Vagalume(), gpt: Gpt = Gpt()) -> None:
        self.vagalume = vagalume
        self.gpt = gpt

    def get_musics(self, query: str) -> list:
        prompt = f"Me recomende 3 musicas relacionadas à '{query}', simplifique a resposta, de forma que me dê apenas os nomes das músicas, separe por vírgulas. Não escreva nada além dos resultados. Também retire as aspas duplas de cada item."
        suggestions = self.gpt.suggestions(prompt)

        musics = []
        for suggestion in suggestions:
            musics.append(self.vagalume.get_mus(suggestion))

        return musics
