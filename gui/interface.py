from domain.player import Player
from domain.states import MoveState
from gui.screen import Screen
import time


class Interface:
    def __init__(self, player1, player2, screen: Screen):
        self.__screen = screen
        self.__player1 = player1
        self.__player2 = player2
        self.__start_time = int(time.time())

    def draw(self):
        color = "red"

        one_hp = (self.__screen.width // 2 - 50) // Player.HP
        rect = self.__screen.canvas.create_rectangle(0, 0, self.__player1.hp * one_hp, 50,
                                                     fill=color)
        self.__screen.add_object(rect)

        rect = self.__screen.canvas.create_rectangle(self.__screen.width - self.__player2.hp * one_hp, 0,
                                                     self.__screen.width, 50,
                                                     fill=color)
        self.__screen.add_object(rect)

        if self.__player1.hp == 0:
            self.__screen.add_object(
                self.__screen.canvas.create_text(self.__screen.width * 0.5, self.__screen.height * 0.5,
                                                 text="Player2 win",
                                                 fill="red", font=('Helvetica', '30', 'bold')))
        if self.__player2.hp == 0:
            self.__screen.add_object(
                self.__screen.canvas.create_text(self.__screen.width * 0.5, self.__screen.height * 0.5,
                                                 text="Player1 win",
                                                 fill="red", font=('Helvetica', '30', 'bold')))

        if self.__screen.frames < 20:
            self.__screen.add_object(
                self.__screen.canvas.create_text(self.__screen.width * 0.5, self.__screen.height * 0.5, text="3",
                                                 fill="white", font=('Helvetica', '80', 'bold')))
        if self.__screen.frames < 40 and self.__screen.frames >= 20:
            self.__screen.add_object(
                self.__screen.canvas.create_text(self.__screen.width * 0.5, self.__screen.height * 0.5, text="2",
                                                 fill="white", font=('Helvetica', '80', 'bold')))
        if self.__screen.frames < 60 and self.__screen.frames >= 40:
            self.__screen.add_object(
                self.__screen.canvas.create_text(self.__screen.width * 0.5, self.__screen.height * 0.5, text="1",
                                                 fill="white", font=('Helvetica', '80', 'bold')))
        if self.__screen.frames < 90 and self.__screen.frames >= 60:
            self.__screen.add_object(
                self.__screen.canvas.create_text(self.__screen.width * 0.5, self.__screen.height * 0.5, text="Fight!",
                                                 fill="white", font=('Helvetica', '80', 'bold')))

        p = 93 -(int(time.time()) - self.__start_time)
        self.__screen.add_object(
            self.__screen.canvas.create_text(self.__screen.width * 0.5, self.__screen.height * 0.06, text=p,
                                             fill="white", font=('Helvetica', '80', 'bold')))
        if p == 0:
            self.__screen.add_object(
              self.__screen.canvas.create_text(self.__screen.width * 0.5, self.__screen.height * 0.5, text="Ничья",
                                                 fill="white", font=('Helvetica', '80', 'bold')))

        if p == -1:
            quit()