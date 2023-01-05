from enum import Enum


class MoveState(Enum):
    START = "start"
    STAND = "stand"
    SIT = "sit"
    JUMP = "jump"


class HitState(Enum):
    NO = "no"
    HAND = "hand"
    LEG = "leg"