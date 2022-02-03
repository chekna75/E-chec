from table import Table


class ListPlayerByName(Table):
    '''Class vue pour afficher le listing des joueurs par par ordre alphabétique'''
    def __init__(self, data):
        super().__init__(title="Liste des joueur par odre alphabetique", items=data)
