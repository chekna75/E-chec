from form import Form


class FormUpdatePlayerRank(Form):
    def __init__(self):
        super().__init__(title="Modifier rang", fields=[("id", "id du joueur", int),
                                                        ("rank", "Nouveau classement", int)])
