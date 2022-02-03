from view import Menu


class PlayersChoiceListing(Menu):
    '''Class de vue pour afficher le listing des joueurs'''
    def __init__(self):
        super().__init__(title="Liste des joueurs", choices=[("Liste des joueurs", 1),
                                                             (" Liste des joueurs par classement", 2),
                                                             (" Liste des joueurs par ordre alphabetique", 3)])
