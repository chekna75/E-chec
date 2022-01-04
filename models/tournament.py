from typing import List
from pydantic import BaseModel
from pydantic.types import PositiveInt
from datetime import datetime
from models.match import Match
from .name import Name
from .turn import Turn
from .timecontrol import TimeControl
from player_manager import player_manager


class Tournament(BaseModel):
    id: PositiveInt
    name: Name
    lieu: Name
    start_date: datetime
    end_date: datetime = None
    turns: List[Turn]
    players: List[PositiveInt]
    description: str
    time_control: TimeControl

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.all_matchs:
            self.generate_first_turn(self.turns)

    def generate_first_turn(self, turn):
        players = [player_manager.find_by_id(id) for id in self.players]
        players = sorted(players, key=lambda x: x.rank)
        groupe1, groupe2 = players[:len(players)//2], players[len(players)//2:] # selection de liste
        for turn in self.turns:
            for i in range(len(groupe1)):
                match = Match(player_one_id=groupe1[i].id, player_two_id=groupe2[i].id)
                turn.matchs.append(match)
                self.get_player_score(players)
            break

    def play(self, view, manager):
        for turn in self.turns:
            print(turn)
            if turn.end_date is None:
                if turn.matchs:
                    turn.play(view=view)
                    manager.save_item(self.id)
                else:
                    self.generate_next_turn(self.turns)

    def generate_next_turn(self, turn):
        players = [player_manager.find_by_id(id) for id in self.players]
        players = sorted(players, key=lambda x: x.rank)
        groupe1, groupe2 = players[:len(players)//2], players[len(players)//2:] # selection de liste
        for turn in self.turns:
            for i in range(len(groupe1)):
                match = Match(player_one_id=groupe1[i].id, player_two_id=groupe2[i].id)
                turn.matchs.append(match)
                break

    def get_player_score(self, id: int):
        score = 0.0
        for turn in self.turns:
            for match in turn.matchs:
                if match.played:
                    if id == match.player_one_id:
                        score += match.score_one.value
                        print(score)
                    elif id == match.player_two_id:
                        score += match.score_two.value
                        print(score)
        print(score)
        return score

    @property
    def all_matchs(self):
        result = []
        for turn in self.turns:
            for match in turn.matchs:
                result.append(match)
        return result

    @property
    def played_matchs(self):
        result = []
        for turn in self.turns:
            for match in turn.matchs:
                if match.played:
                    result.append(match)
        return result

    def __str__(self) -> str:
        return f'{self.name} {self.lieu} {self.start_date} {self.end_date} {self.description}'
