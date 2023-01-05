class Object:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def draw(self, canvas):
        pass

    def move_by(self, vx, vy):
        self._x += vx
        self._y += vy

    def move_to(self, x, y):
        self._x = x
        self._x = y
