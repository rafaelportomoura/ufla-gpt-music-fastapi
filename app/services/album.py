    
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
    
    
    def get_albums(self, query: str) -> list:
        suggestions = self.gpt.suggestions(query)
        
        albums = []
        for suggestion in suggestions:
            albums.append(
                self.vagalume.get_album(suggestion)
            )
        return albums