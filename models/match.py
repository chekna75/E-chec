from pydantic.types import PositiveInt
from pydantic import BaseModel
from .result import Result


class Match(BaseModel):
    player_one_id: PositiveInt
    player_two_id: PositiveInt
    result: Result = None
