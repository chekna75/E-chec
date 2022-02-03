from view import Menu


class ChoiceWinner(Menu):
    def __init__(self, joueur1, joueur2):
        choices = [(str(joueur1) + " a gagné", 1.0), (str(joueur2) + " a gagné", 0.0), ("match nul", 0.5)]
        super().__init__(title="Choissisez le gagnant", choices=choices)
