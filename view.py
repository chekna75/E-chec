import os


class View:
    '''afficher titre et contenu'''
    def __init__(self, title: str, content: str = "", blocking: bool = False):
        self.title = title
        self.content = content
        self.blocking = blocking

    def display(self):
        os.system("clear")
        print(self.title)
        print("__________________")
        print(self.content)
        if self.blocking:
            input()


# #view = View(title="A", content="B")
# view.display()


class Menu(View):
    '''Reprendre les capacité de view et pouvoir faire un choix 
    parmis les options'''
    def __init__(self, title, choices):
        self.choices = choices
        content = "\n".join([f'{nb}) {el}' for nb, el in enumerate(choices,
                                                                   start=1)])
        super().__init__(title, content)

    def display(self):
        while True:
            super().display()
            try:
                selection = int(input("Faire un choix : "))
                if 0 < selection <= len(self.choices):
                    return selection
            except ValueError:
                pass


class ChoiceWinner(Menu):
    def __init__(self, joueur1, joueur2):
        choices = [str(joueur1) + "ème rang a gagné", str(joueur2) + "ème rang a gagné", "match nul"]
        super().__init__(title="Choissisez le gagnant", choices=choices)
