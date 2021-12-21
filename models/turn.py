from pydantic import BaseModel
from .name import Name
from .match import Match
from datetime import datetime
from typing import List
from player_manager import player_manager
from models.result import Result


class Turn(BaseModel):
    name: Name
    start_date: datetime = datetime.today()
    end_date: datetime = None
    matchs: List[Match] = []

    def play(self, view):
        for match in self.matchs:
            if match.result is None:
                player_one = player_manager.find_by_id(match.player_one_id)
                player_two = player_manager.find_by_id(match.player_two_id)
                choice = view(joueur1=player_one, joueur2=player_two).display()
                if choice == 1:
                    match.result = Result.PlayerOneWins
                elif choice == 2:
                    match.result = Result.PlayerTwoWins
                else:
                    match.result = Result.Draw
        self.end_date = datetime.today()
