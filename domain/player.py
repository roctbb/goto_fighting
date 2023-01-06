from domain.object import Object
from domain.skin import Skin
from domain.states import MoveState, HitState, Direction
from gui.screen import Screen
from tkinter import NW


class Player(Object):
    LEG_POWER = 10
    HAND_POWER = 5
    SHOT_POWER = 15

    JUMP_SPEED = 37

    HIT_TIME = 5

    def __init__(self, direction, screen: Screen, skin: Skin):
        if direction == Direction.LEFT:
            x, y = skin.width // 2, screen.height - skin.height
        else:
            x, y = screen.width - int(skin.width * 1.5), screen.height - skin.height

        super().__init__(x, y, skin.width, skin.height, screen)

        self.__initial_height = skin.height
        self.__hp = 100
        self.__direction = direction
        self.__skin = skin
        self.__speed = 10
        self.__move_state = MoveState.STAND
        self.__hit_state = HitState.NO
        self.__hit_timer = 0
        self.__jump_speed = 0
        self.__move_speed = 0

    @property
    def hp(self):
        return self.__hp

    @property
    def direction(self):
        return self.__direction

    # получить урон
    def make_damage(self, amount):
        self.__hp = max(0, self.__hp - amount)

    # навыки
    def hit_hand(self):
        self.__hit_state = HitState.HAND
        self.__hit_timer = self.HIT_TIME

    def hit_leg(self):
        self.__hit_state = HitState.LEG
        self.__hit_timer = self.HIT_TIME

    def shot(self):
        self.__hit_state = HitState.SHOT
        self.__hit_timer = self.HIT_TIME

    def is_attacking(self):
        if self.__hit_state != HitState.NO:
            return True
        return False

    @property
    def attack_power(self):
        if not self.is_attacking:
            return 0
        if self.__hit_state == HitState.LEG:
            return self.LEG_POWER
        if self.__hit_state == HitState.HAND:
            return self.HAND_POWER
        if self.__hit_state == HitState.SHOT:
            return self.SHOT_POWER
    # перемещение
    def sit(self):
        if self.__move_state == MoveState.STAND:
            self.__move_state = MoveState.SIT
            self._height = self.__initial_height // 2
            self.move_by(0, self._height)

    def stand(self):
        if self.__move_state == MoveState.SIT:
            self._height = self.__initial_height
            self.__move_state = MoveState.STAND
            self.move_by(0, self._height)

    def jump(self):
        if self.__jump_speed == 0:
            self.stand()

            self.__jump_speed = -self.JUMP_SPEED
            self.move_by(0, self.__jump_speed)
            self.__move_state = MoveState.JUMP

    def right(self):
        self.__move_speed = 10

    def left(self):
        self.__move_speed = -10

    def stop(self):
        self.__move_speed = 0

    def flip(self):
        if self.__direction == Direction.LEFT:
            self.__direction = Direction.RIGHT
        else:
            self.__direction = Direction.LEFT

    def update(self):
        if self.__hit_timer == 0:
            self.__hit_state = HitState.NO
        else:
            self.__hit_timer -= 1

        if self.y + self.height == self._screen.height:
            self.__jump_speed = 0
            if self.__move_state == MoveState.JUMP:
                self.__move_state = MoveState.STAND
        else:
            self.move_by(0, self.__jump_speed)
            self.__jump_speed += self.GRAVITY

        self.move_by(self.__move_speed, 0)

    # графика
    def draw(self):
        self.update()

        rect = self._screen.canvas.create_image(self.x, self.y,
                                                image=self.__skin.get_image(self.direction, self.__move_state,
                                                                            self.__hit_state), anchor=NW)
        self._screen.add_object(rect)