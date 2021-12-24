from typing import Any, Dict, List, Tuple
from view import View


class Form(View):

    def __init__(self, title: str, fields: List[Tuple[str, str, Any]]) -> None:
        super().__init__(title=title)
        self.fields = fields

    def display(self):
        super().__init__(self)
        data = {}
        for field_name, field_desc, field_type in self.fields:
            while True:
                try:
                    field_value = input(field_desc + " ? ")
                    data[field_name] = field_type(field_value)
                    break
                except ValueError:
                    pass
        return self.post_process(data)
    
    def post_process(self, data: Dict):
        return data
