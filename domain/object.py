class Object:
    GRAVITY = 3

    def __init__(self, x, y, w, h, screen):
        self._x = x
        self._y = y
        self._width = w
        self._height = h
        self._screen = screen

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def draw(self):
        pass

    def move_by(self, vx, vy):
        if vx > 0:
            if self.x + vx + self.width <= self._screen.width:
                self._x += vx
            else:
                self._x = self._screen.height - self.height
        elif vx < 0:
            if self.x + vx >= 0:
                self._x += vx
            else:
                self._x = 0

        if vy > 0:
            if self.y + vy + self.width <= self._screen.width:
                self._y += vy
            else:
                self._y = self._screen.height - self.height
        elif vy < 0:
            if self.y + vy >= 0:
                self._y += vy
            else:
                self._y = 0


    def move_to(self, x, y):
        self._x = x
        self._x = y
