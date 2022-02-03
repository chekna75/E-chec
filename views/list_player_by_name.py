from table import Table


class ListPlayerByName(Table):
    def __init__(self, data):
        super().__init__(title="Liste des joueur par odre alphabetique", items=data)
