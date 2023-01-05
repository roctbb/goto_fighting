from domain.object import Object
from domain.skin import Skin


class Player(Object):
    def __init__(self, x: int, y: int, direction: str, skin: Skin):
        super().__init__(x, y)
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
        self._y += 1

    def jump(self):
        self._y -= 1

    def forward(self):
        self._x += 1

    def backward(self):
        self._x -= 1

    # графика
    def draw(self, canvas):
        self.clear(canvas)
        self._add_object(canvas.create_rectangle(self.x, self.y, self.x + 100,self.y + 100, fill="ivory3"))
