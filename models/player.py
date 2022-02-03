from pydantic import BaseModel
from pydantic.types import PositiveInt
from datetime import date
from .gender import Gender
from .name import Name


class Player(BaseModel):
    '''Class model pour le model d'un joueur'''
    id: PositiveInt
    first_name: Name
    last_name: Name
    birthdate: date
    gender: Gender
    rank: PositiveInt

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.rank}'
