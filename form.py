from typing import List, Tuple
from view import View


class Form(View):

    def __init__(self, title: str, fields: List[Tuple[str, str]]) -> None:
        super().__init__(title=title)
        self.fields = fields

    def display(self):
        super().__init__(self)
        data = {}
        for field_name, field_desc in self.fields:
            field_value = input(field_desc + " ? ")
            data[field_name] = field_value
        return data
