from dataclasses import dataclass
from gui.states import *


@dataclass
class Attack:
    move_state: MoveState = None
    hit_state: HitState = None
    power: int = 0
