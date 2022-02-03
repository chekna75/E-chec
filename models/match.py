from pydantic.types import PositiveInt
from pydantic import BaseModel
from .result import Result


class Match(BaseModel):
    '''Class model d'un match'''
    player_one_id: PositiveInt
    player_two_id: PositiveInt
    score_one: Result = None

    def play(self, view_class, player_manager):
        '''Fonction qui permttre de jouer un match si il est pas encore jouer'''
        if not self.played:
            player_one = player_manager.find_by_id(self.player_one_id)
            player_two = player_manager.find_by_id(self.player_two_id)
            choice = view_class(joueur1=player_one, joueur2=player_two).display()
            self.score_one = Result(choice)

    def __eq__(self, other):
        return sorted([self.player_one_id, self.player_two_id]) == sorted([other.player_one_id, other.player_two_id])

    @property
    def score_two(self):
        return Result(1.0 - self.score_one.value)

    @property
    def played(self):
        return self.score_one is not None
