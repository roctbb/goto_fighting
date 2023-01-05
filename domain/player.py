import time

from domain.object import Object
from domain.skin import Skin
from gui.screen import Screen


class Player(Object):
    def __init__(self, x: int, y: int, direction: str, screen: Screen, skin: Skin):
        super().__init__(x, y, 100, 100, screen)
        self.__hp = 100
        self.__direction = direction
        self.__skin = skin
        self.__speed = 10
        self.__jump_speed = 25

    @property
    def hp(self):
        return self.__hp

    # получить урон
    def damage(self, amount):
        self.__hp = max(0, self.__hp - amount)

    # навыки
    def hit_hand(self):
        pass

    def hit_leg(self):
        pass

    # перемещение
    def sit_down(self):


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
        if self.y + self.height == self._screen.height:
            self.__jump_speed = 0
        else:
            self.move_by(0, self.__jump_speed)
            self.__jump_speed += self.GRAVITY


    # графика
    def draw(self):
        self.update()
        rect = self._screen.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="ivory3")
        self._screen.add_object(rect)
