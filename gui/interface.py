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

        one_hp = (self.__screen.width // 2 - 50) // 100
        rect = self.__screen.canvas.create_rectangle(0, 0, self.__player1.hp * one_hp, 100,
                                                    fill=color)
        self.__screen.add_object(rect)

        # self.__screen.width
        # self.__screen.height

        rect = self.__screen.canvas.create_rectangle(self.__screen.width - self.__player2.hp * one_hp, 0, self.__screen.width, 100,
                                                    fill=color)
        self.__screen.add_object(rect)



