from table import Table
from tournament_manager import tournament_manager as tm


class ViewListTournament(Table):
    def __init__(self):
        super().__init__(title="Liste des tournois", items=tm.find_all())
