import os
from typing import List


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
    def __init__(self, title: str, choices: List[str]):
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
        choices = [(str(joueur1) + " a gagné", 1.0), (str(joueur2) + " a gagné", 0.0), ("match nul", 0,5)]
        super().__init__(title="Choissisez le gagnant", choices=choices)
