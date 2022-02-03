from table import Table


class ListPlayerByRank(Table):
    '''Class vue pour le listing des joueurs par ordre de rank'''
    def __init__(self, data):
        super().__init__(title="Liste des joueur par classement", items=data)
