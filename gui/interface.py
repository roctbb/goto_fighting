from gui.screen import Screen
import time


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

        rect = self.__screen.canvas.create_rectangle(self.__screen.width - self.__player2.hp * one_hp, 0,
                                                     self.__screen.width, 100,
                                                     fill=color)
        self.__screen.add_object(rect)

        if self.__player1.hp == 0:
            self.__screen.canvas.create_text(self.__screen.width * 0.5, self.__screen.height * 0.5, text="Player2 win",
                                             fill="red", font=('Helvetica', '30', 'bold'))
        if self.__player2.hp == 0:
            self.__screen.canvas.create_text(self.__screen.width * 0.5, self.__screen.height * 0.5, text="Player1 win",
                                             fill="red", font=('Helvetica', '30', 'bold'))
