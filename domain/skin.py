import pygame

from domain.flying_ball import Ball
from domain.states import *
from gui.animation import Animation
from copy import copy

from gui.common import asset_path
from gui.gif_animation import GifAnimation


class Skin:
    def __init__(self, description):
        self.__animations = {}
        self.__old_state = None
        self.__width = description["width"]
        self.__height = description["height"]
        self.__bullet_animation = GifAnimation(description["bullet"], (Ball.WIDTH, Ball.HEIGHT))
        self.__description = description
        self.__name = description['name']

        self.__sounds = {
            key: pygame.mixer.Sound(asset_path(value)) for key, value in self.__description["sounds"].items()
        }

        for direction in [Direction.LEFT, Direction.RIGHT]:
            for move_state in [MoveState.STAND, MoveState.START, MoveState.JUMP, MoveState.SIT, MoveState.WIN, MoveState.LOSS]:
                if move_state.value in description:
                    move_description = description[move_state.value]
                    for hit_state in [HitState.NO, HitState.LEG, HitState.HAND, HitState.SHOT, HitState.BLOCK]:
                        if hit_state.value in move_description:
                            animation_description = move_description[hit_state.value]
                            if direction.value != description['orientation']:
                                flip = True
                            else:
                                flip = False
                            if move_state == MoveState.SIT or move_state == MoveState.LOSS:
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
    def name(self):
        return self.__name

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

    @property
    def bullet_animation(self):
        return copy(self.__bullet_animation)

    def play_sound(self, sound):
        # pygame.mixer.music.load(asset_path(self.__description["sounds"]["start"]))
        # pygame.mixer.music.play(1)
        if sound in self.__sounds:
            self.__sounds[sound].play()
