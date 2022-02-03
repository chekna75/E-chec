from view import Menu


class MainMenu(Menu):
    def __init__(self):
        super().__init__(title="Menu Principal", choices=[("Creer un joueur", 1),
                                                          ("Creer un tournois", 2),
                                                          ("Liste des joueur", 3),
                                                          ("Lister un tournois", 4),
                                                          ("Liste des joueur par classement", 5),
                                                          ("Afficher les rapport", 6),
                                                          ("Modifier un joueur", 7),
                                                          ("Reprendre un tournois", 8)])
