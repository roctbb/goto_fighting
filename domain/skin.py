from domain.states import *
from gui.animation import Animation


class Skin:
    def __init__(self, description):
        self.__animations = {}
        self.__old_state = None
        self.__width = description["width"]
        self.__height = description["height"]

        for direction in [Direction.LEFT, Direction.RIGHT]:
            for move_state in [MoveState.STAND, MoveState.START, MoveState.JUMP, MoveState.SIT]:
                if move_state.value in description:
                    move_description = description[move_state.value]
                    for hit_state in [HitState.NO, HitState.LEG, HitState.HAND, HitState.SHOT]:
                        if hit_state.value in move_description:
                            animation_description = move_description[hit_state.value]
                            if direction.value != description['orientation']:
                                flip = True
                            else:
                                flip = False
                            if move_state == MoveState.SIT:
                                self.__animations[
                                    (direction, move_state, hit_state)] = Animation(animation_description,
                                                                                    (self.width, self.height // 2),
                                                                                    flip)
                            else:
                                self.__animations[
                                    (direction, move_state, hit_state)] = Animation(animation_description,
                                                                                    (self.width, self.height),
                                                                                    flip)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def get_image(self, direction, movement, hit_state):
        if (direction, movement, hit_state) not in self.__animations:
            return

        if self.__old_state != (direction, movement, hit_state):
            self.__old_state = (direction, movement, hit_state)
            self.__animations[(direction, movement, hit_state)].reset()

        return self.__animations[(direction, movement, hit_state)].get_image()
