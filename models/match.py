from pydantic.types import PositiveInt
from pydantic import BaseModel
from .result import Result


class Match(BaseModel):
    player_one_id: PositiveInt
    player_two_id: PositiveInt
    score_one: Result = None

    @property
    def score_two(self):
        return Result(1.0 - self.score_one.value)

    @property
    def played(self):
        return self.score_one is not None
