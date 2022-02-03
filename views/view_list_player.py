from table import Table
from player_manager import player_manager as pm


class ViewListPlayer(Table):
    def __init__(self):
        super().__init__(title="Liste des joueurs", items=pm.find_all())
