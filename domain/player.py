from domain.object import Object
from domain.skin import Skin


class Player(Object):
    def __init__(self, x: int, y: int, direction: str, skin: Skin):
        self.__init__(x, y)
        self.__hp = 100
        self.__direction = direction
        self.__skin = skin

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
        pass

    def jump(self):
        pass

    def forward(self):
        pass

    def backward(self):
        pass
