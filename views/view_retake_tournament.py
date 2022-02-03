from form import Form


class ViewRetakeTournament(Form):
    '''Class vue qui permet de reprendre un tournoi'''
    def __init__(self):
        super().__init__(title="Reprendre un tournoi", fields=[("id", "id du tournoi", str)])
