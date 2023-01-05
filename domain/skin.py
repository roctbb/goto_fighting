from domain.states import *
from gui.animation import Animation


class Skin:
    def __init__(self, description):
        self.__animations = {}

        for direction in [Direction.LEFT, Direction.RIGHT]:
            for move_state in [MoveState.STAND, MoveState.START, MoveState.JUMP, MoveState.SIT]:
                if move_state.value in description:
                    move_description = description[move_state.value]
                    for hit_state in [HitState.NO, HitState.LEG, HitState.HAND]:
                        if hit_state.value in move_description:
                            animation_description = move_description[hit_state.value]
                            self.__animations[
                                (direction, move_state, hit_state)] = Animation(animation_description)

    def get_image(self, direction, movement, hit_state):
        return self.__animations[(direction, movement, hit_state)].get_image()
