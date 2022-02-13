from view import Menu


class MainMenu(Menu):
    '''Class vue poir afficher le menu principal'''
    def __init__(self):
        super().__init__(title="Menu Principal", choices=[("Creer un joueur", 1),
                                                          ("Creer un tournoi", 2),
                                                          ("Lister les joueurs", 3),
                                                          ("Lister un tournoi", 4),
                                                          ("Lister les joueur par classement", 5),
                                                          ("Modifier un joueur", 6),
                                                          ("Reprendre un tournois", 7),
                                                          ("test", 8)])
