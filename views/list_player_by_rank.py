from table import Table


class ListPlayerByRank(Table):
    def __init__(self, data):
        super().__init__(title="Liste des joueur par classement", items=data)
