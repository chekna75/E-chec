from form import Form


class ViewRetakeTournament(Form):
    def __init__(self):
        super().__init__(title="Reprendre un tournoi", fields=[("id", "id du tournoi", str)])
