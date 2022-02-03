from form import Form
from models.gender import Gender


class ViewCreatePlayers(Form):
    '''Cette class est une vue pour la création du joueur'''
    def __init__(self):
        super().__init__(title="Crée un joueur", fields=[("first_name", "prénom", str),
                                                         ("last_name", "nom", str),
                                                         ("birthdate", "date de naissance(AAAA-MM-JJ)", str),
                                                         ("gender", "genre", Gender),
                                                         ("rank", "rang", int)])
