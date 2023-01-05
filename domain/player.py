from domain.object import Object
from domain.skin import Skin
from domain.states import MoveState, HitState
from gui.screen import Screen


class Player(Object):
    LEG_POWER = 10
    HAND_POWER = 5

    def __init__(self, x: int, y: int, direction: str, screen: Screen, skin: Skin):
        super().__init__(x, y, 100, 100, screen)
        self.__hp = 100
        self.__direction = direction
        self.__skin = skin
        self.__speed = 10
        self.__move_state = MoveState.STAND
        self.__hit_state = HitState.NO
        self.__hit_timer = 0
        self.__jump_speed = 25
        self._width = 100
        self._height = 100

    @property
    def hp(self):
        return self.__hp

    # получить урон
    def make_damage(self, amount):
        self.__hp = max(0, self.__hp - amount)

    # навыки
    def hit_hand(self):
        self.__hit_state = HitState.HAND
        self.__hit_timer = 20

    def hit_leg(self):
        self.__hit_state = HitState.LEG
        self.__hit_timer = 20

    @property
    def is_attacking(self):
        if self.__hit_state != HitState.NO:
            return True
        return False

    def attack_power(self):
        if not self.is_attacking:
            return 0
        if self.__hit_state == HitState.LEG:
            return self.LEG_POWER
        if self.__hit_state == HitState.HAND:
            return self.HAND_POWER

    # перемещение
    def sit(self):
        if self.__move_state == MoveState.STAND:
            self.__move_state = MoveState.SIT
            self._height = self._height // 2
            self.move_by(0, self._height // 2)
    def stand(self):
        if self.__move_state == MoveState.SIT:
            self._height = self._height * 2
            self.__move_state = MoveState.STAND
            self.move_by(0, self._height // 2)
    def jump(self):
        if self.__jump_speed == 0:
            self.__jump_speed = -25
            self.move_by(0, self.__jump_speed)
        else:
            pass

    def right(self):
        self.move_by(self.__speed, 0)

    def left(self):
        self.move_by(-self.__speed, 0)

    def update(self):
        if self.__hit_timer == 0:
            self.__hit_state = HitState.NO
        else:
            self.__hit_timer -= 1

        if self.y + self.height == self._screen.height:
            self.__jump_speed = 0
        else:
            self.move_by(0, self.__jump_speed)
            self.__jump_speed += self.GRAVITY

    # графика
    def draw(self):
        self.update()

        color = "green"
        if self.is_attacking:
            color = "red"
        rect = self._screen.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height,
                                                    fill=color)
        self._screen.add_object(rect)
