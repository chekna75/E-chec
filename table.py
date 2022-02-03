from typing import Any, List
from view import View


class Table(View):
    '''Class table'''
    def __init__(self, title, items: List[Any]) -> None:
        content = "\n".join([str(item) for item in items])
        print(content)
        super().__init__(title, content, blocking=True)
