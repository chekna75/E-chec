import re


class Name(str):
    def __new__(cls, v):
        if not re.match(r"^[A-Za-z \-éèëê']{2,20}$", v):
            raise ValueError('Nom incorrect')
        return str.__new__(cls, v.title())