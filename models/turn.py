from pydantic import BaseModel
from .name import Name
from .match import Match
from datetime import datetime
from typing import List


class Turn(BaseModel):
    name: Name
    start_date: datetime = datetime.today()
    end_date: datetime = None
    matchs: List[Match] = []

    def play(self, view_class, player_manager):
        for match in self.matchs:
            match.play(view_class, player_manager)
            if match.score_one is not None:
                self.end_date = datetime.today()
