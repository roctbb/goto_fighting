from domain.object import Object
from domain.skin import Skin
from domain.states import MoveState, HitState, Direction
from gui.screen import Screen
class Interface:
    def __init__(self, player1, player2, screen: Screen):
        self.__screen = screen
        self.__player1 = player1
        self.__player2 = player2

    def draw(self):
        color = "red"
        rect = self.__screen.canvas.create_rectangle(0, 0, 200, 50,
                                                    fill=color)
        self.__screen.add_object(rect)

        # self.__screen.width
        # self.__screen.height

        rect = self.__screen.canvas.create_rectangle(440, 50, 644, 0,
                                                    fill=color)
        self.__screen.add_object(rect)




