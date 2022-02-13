from form import Form


class List_players_rank_controller_Tournament(Form):
    '''Class vue pour afficher la modification du rank des joueurs'''
    def __init__(self):
        super().__init__(title="Liste des joueurs", fields=[("id", "id du tournoi", int)])
