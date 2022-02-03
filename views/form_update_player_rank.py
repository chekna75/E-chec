from form import Form


class FormUpdatePlayerRank(Form):
    '''Class vue pour afficher la modification du rank des joueurs'''
    def __init__(self):
        super().__init__(title="Modifier rang", fields=[("id", "id du joueur", int),
                                                        ("rank", "Nouveau classement", int)])
