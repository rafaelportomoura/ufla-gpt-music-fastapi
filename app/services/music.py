from services.vagalume import Vagalume
from services.gpt import Gpt
class Music:
    def __init__(
        self,
        vagalume : Vagalume=Vagalume(),
        gpt : Gpt=Gpt()
    ) -> None:
        self.vagalume = vagalume
        self.gpt = gpt

    def get_musics(self, query: str) -> list:
        suggestions = self.gpt.suggestions(query)

        musics = []
        for suggestion in suggestions:
            musics.append(
                self.vagalume.get_art_mus(suggestion)
            )

        return musics