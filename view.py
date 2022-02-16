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


class Menu(View):
    '''Reprendre les capacité de view et pouvoir faire un choix parmis les options'''
    def __init__(self, title: str, choices: List[str]):
        self.choices = choices
        content = "\n".join([f'{nb}) {el[0]}' for nb, el in enumerate(choices, start=1)])
        super().__init__(title, content)

    def display(self):
        while True:
            super().display()
            try:
                selection = int(input("Faire un choix : "))
                if 0 < selection <= len(self.choices):
                    return self.choices[selection-1][1]
                else:
                    raise ValueError
            except (ValueError, IndexError) as e:
                input(str(e))
