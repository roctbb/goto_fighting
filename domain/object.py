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

    def intersects_with(self, object):
        x1, y1, x2, y2 = self.x, self.y, self.x + self.width, self.y + self.height
        i1, j1, i2, j2 = object.x, object.y, object.x + object.width, object.y + object.height

        if (x1 < i1 < x2 or x1 < i2 < x2) and (y1 < j1 < y2 or y1 < j2 < y2):
            return True
        return False

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
                self._x = self._screen.width - self.width
        elif vx < 0:
            if self.x + vx >= 0:
                self._x += vx
            else:
                self._x = 0

        if vy > 0:
            if self.y + vy + self.height <= self._screen.height:
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
