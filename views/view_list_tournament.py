from table import Table
from tournament_manager import tournament_manager as tm


class ViewListTournament(Table):
    '''Class vue pour la lsite des tournois'''
    def __init__(self):
        super().__init__(title="Liste des tournois", items=tm.find_all())
