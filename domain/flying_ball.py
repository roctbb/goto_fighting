from domain.object import Object


class Ball(Object):
    def __init__(self):
        super().__init__()
        self.__speed = 15


