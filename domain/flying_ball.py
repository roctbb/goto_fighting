from domain.object import Object
from domain.states import Direction


class Ball(Object):

    SPEED = 30
    WIDTH = 75
    HEIGHT = 75
    POWER = 200

    def __init__(self, x, y, direction, animation, screen):
        super().__init__(x, y, self.WIDTH, self.HEIGHT, direction, screen)
        self.__speed = self.SPEED
        self.__animation = animation

    def draw(self):
        ball = self._screen.canvas.create_image(self.x, self.y, image=self.__animation.get_image())

        self._screen.add_object(ball)


    def update(self):
        if self._direction == Direction.LEFT:
            self._x += -self.__speed
        if self._direction == Direction.RIGHT:
            self._x += self.__speed


    @property
    def is_dead(self):
        return self._x < 0 or self._x + self.width > self._screen.width

    def die(self):
        self._x = -100

    @property
    def attack_power(self):
        return self.POWER
