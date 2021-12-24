from typing import List
from pydantic import BaseModel
from pydantic.types import PositiveInt
from datetime import datetime
from models.match import Match
from view import ChoiceWinner
from .name import Name
from .turn import Turn
from .timecontrol import TimeControl
from player_manager import player_manager
from manager import Manager


class Tournament(BaseModel):
    id: PositiveInt
    name: Name
    lieu: Name
    start_date: datetime
    end_date: datetime = None
    number_of_turns: int = 4
    turns: List[Turn] = []
    players: List[PositiveInt]
    description: str
    time_control: TimeControl

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.turns:
            self.generate_first_turn()

    def generate_first_turn(self):
        players = [player_manager.find_by_id(id) for id in self.players]
        players = sorted(players, key=lambda x: x.rank)
        groupe1, groupe2 = players[:len(players)//2], players[len(players)//2:] # selection de liste
        # print(groupe1, groupe2)
        turn = Turn(name="Round1")
        for i in range(len(groupe1)):
            match = Match(player_one_id=groupe1[i].id, player_two_id=groupe2[i].id)
            turn.matchs.append(match)
            print(match)
        self.turns.append(turn)
        print(turn.matchs)
        
        input("")

        # if turn.end_date is not None:
        #     print("Generating next turn")
        #     self.generate_next_turn()
        # else:
        #     print("Veuillez entrez tout les resultats")
        #     print(match)

    def play(self, view, manager):
        for turn in self.turns:
            print(turn)
            if turn is not None:
                turn.play(view=view)
                manager.save_item(self.id)

    def generate_next_turn(self):
        players = [player_manager.find_by_id(id) for id in self.players]
        players = sorted(players, key=lambda x: x.rank)
        groupe1, groupe2 = players[:len(players)//2], players[len(players)//2:] # selection de liste
        # print(groupe1, groupe2)
        turn = Turn(name="Round1")
        for i in range(len(groupe1)):
            match = Match(player_one_id=groupe1[i].id, player_two_id=groupe2[i].id)
            turn.matchs.append(match)
            print(match)
        self.turns.append(turn)
        print(turn.matchs)
        input("")
        
    def generate_turn(self):
        turn_nb = self.turns
        print(turn_nb)
        for turn in self.turns:
            if turn == 1:
                self.generate_first_turn()
            elif turn != 1:
                self.generate_next_turn()
            elif turn > 4:
                print("tournois fini")
    
    def get_player_score(self, id: int):
        score = 0.0
        for turn in self.turns:
            for match in turn.matches:
                if match.result is not None:
                    if id == match.player_one_id:
                        score += match.score
                    elif id == match.player_two_id:
                        score += match.score
            
        return score

    def __str__(self) -> str:
        return f'{self.name} {self.lieu} {self.start_date} {self.end_date} {self.description}'
