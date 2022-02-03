from view import Menu


class PlayersChoiceListing(Menu):
    def __init__(self):
        super().__init__(title="Liste des joueurs", choices=[("Liste des joueurs", 1),
                                                             (" Liste des joueurs par classement", 2),
                                                             (" Liste des joueurs par ordre alphabetique", 3)])
