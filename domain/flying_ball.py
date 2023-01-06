from domain.object import Object
from domain.states import Direction


class Ball(Object):

    SPEED = 15
    WIDTH = 50
    HEIGHT = 50

    def __init__(self, x, y, direction, screen):
        super().__init__(x, y, self.WIDTH, self.HEIGHT, screen)
        self.__speed = self.SPEED
        self.__direction = direction

    def draw(self):
        if self.__direction == Direction.LEFT:
            ball = self._screen.canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height, fill="red")
        else:
            ball = self._screen.canvas.create_oval(self.x, self.y, self.x + self.width, self.y + self.height,
                                                   fill="red")
        self._screen.add_object(ball)


    def update(self):
        if self.__direction == Direction.LEFT:
            self._x += -self.__speed
        if self.__direction == Direction.RIGHT:
            self._x += self.__speed

        print(self._x)

    @property
    def is_dead(self):
        return self._x < 0 or self._x + self.width > self._screen.width

    def die(self):
        self._x = -100

    @property
    def attack_power(self):
        return 5
