from enum import Enum


class MoveState(Enum):
    START = "start"
    WIN = "win"
    LOSS = "loss"
    STAND = "stand"
    SIT = "sit"
    JUMP = "jump"


class HitState(Enum):
    NO = "no"
    HAND = "hand"
    LEG = "leg"
    SHOT = 'shot'
    BLOCK = 'block'

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
