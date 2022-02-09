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
    '''Class model pour tournois'''
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
            self.generate_first_turn()

    def generate_first_turn(self):
        '''Fonction pour la génération du premier tour et la création des premier match'''
        players = [player_manager.find_by_id(id) for id in self.players]
        players = sorted(players, key=lambda x: x.rank)
        groupe1, groupe2 = players[:len(players)//2], players[len(players)//2:]
        self.turns[0].matchs = [Match(player_one_id=p1.id, player_two_id=p2.id) for p1, p2 in zip(groupe1, groupe2)]

    def play(self, view_class, player_manager, tournament_manager):
        '''Fonction pour jouer'''
        for turn_nb, turn in enumerate(self.turns):
            if turn.end_date is None:
                if turn.matchs:
                    turn.play(view_class, player_manager)
                    tournament_manager.save_item(self.id)
                else:
                    self.generate_next_turn(turn_nb)
                    turn.play(view_class, player_manager)
                    tournament_manager.save_item(self.id)

    def generate_next_turn(self, turn_nb):
        '''Fonction pour la génération des prochain tour'''
        self.turns[turn_nb].start_date = datetime.today()
        players = [player_manager.find_by_id(id) for id in self.players]
        players = sorted(players, key=lambda x: (-self.get_player_score(x.id), -x.rank))
        while players:
            p1 = players.pop(0)
            m = self.create_match(players, p1, turn_nb)
            self.turns[turn_nb].matchs.append(m)

    def get_player_score(self, id: int):
        '''Fonction pour définir le score du match'''
        score = 0.0
        for turn in self.turns:
            for match in turn.matchs:
                if match.played:
                    if id == match.player_one_id:
                        score += match.score_one.value
                    elif id == match.player_two_id:
                        score += match.score_two.value

        return score

    @property
    def all_matchs(self):
        '''Fonction pour avoir tout les matchs'''
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

    def create_match(self, players, p1, turn_nb):
        '''Fonction pour la création des match'''
        for p2 in players:
            m = Match(player_one_id=p1.id, player_two_id=p2.id)
            if m not in self.turns[turn_nb].matchs:
                players.pop(players.index(p2))
                return m
        p2 = players.pop(0)
        m = Match(player_one_id=p1.id, player_two_id=p2.id)
        return m

    def __str__(self) -> str:
        return f'{self.name} {self.lieu} {self.start_date} {self.end_date} {self.description}'
