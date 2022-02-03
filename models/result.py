from enum import Enum


class Result(Enum):
    '''Class model pour le result'''
    PlayerOneWins = 1.0
    PlayerTwoWins = 0.0
    Draw = 0.5
