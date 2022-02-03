from typing import Dict
from form import Form
from models.timecontrol import TimeControl
from datetime import datetime


class CreateNewTournamentForm(Form):
    '''Class pour la création d'un tournois'''
    def __init__(self):
        super().__init__(
            title="Crée un Tournois",
            fields=[("name", "Nom du tournois", str),
                    ("lieu", "Lieu", str),
                    ("start_year", "Année de début", int),
                    ("start_month", "mois du début", int),
                    ("start_day", "jour du début", int),
                    ("start_hour", "heure du début", int),
                    ("start_minute", "minute du début", int),
                    ("number_of_turns", "Nombre de tour", int),
                    ("number_of_players", "Nombre de joueur", int),
                    ("description", "description", str),
                    ("time_control", "Controle du temps", TimeControl)])

    def post_process(self, data: Dict):
        '''Permet de découper l'affichage et la saisie'''
        data["start_date"] = datetime(year=data["start_year"], month=data["start_month"], day=data["start_day"],
                                      hour=data["start_hour"], minute=data["start_minute"])
        data["players"] = []
        for _ in range(data["number_of_players"]):
            player_data = Form(title="Nombre de joueur", fields=[("id", "id du joueur", int)]).display()
            data["players"].append(player_data["id"])
        data["turns"] = [{"name": f'tour{turn_nb}'} for turn_nb in range(1, data["number_of_turns"]+1)]
        return data
