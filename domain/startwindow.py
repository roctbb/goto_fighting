from tkinter import *
from domain.game import Game
from gui.screen import Screen

import os


class StartWindow:
    def __init__(self, screen: Screen):
        self.__screen = screen

        self.on_start = None



    def __click(self, event):
        print(event)
        if event.x > self.__screen.width // 4 and event.x < 2 * self.__screen.width // 4 and self.__screen.height // 4 < event.y < 2 * self.__screen.height // 4:
            self.start()
        elif event.x > self.__screen.width // 4 and event.x < 2 * self.__screen.width // 4 and 2 * self.__screen.height // 4 < event.y < 3 * self.__screen.height // 4:
            self.exit()


    def draw(self):
        self.__screen.canvas.bind("<Button-1>", self.__click)
        self.__screen.clear()
        print(self.__screen.width // 4, self.__screen.height // 4,
                                              2 * self.__screen.width // 4, 2 * self.__screen.height // 4)
        self.__screen.add_object(self.__screen.canvas.create_rectangle(self.__screen.width // 4, self.__screen.height // 4,
                                              2 * self.__screen.width // 4, 2 * self.__screen.height // 4, fill="blue"))

        self.__screen.add_object(
            self.__screen.canvas.create_rectangle(self.__screen.width // 4, 2 * self.__screen.height // 4,
                                                  2 * self.__screen.width // 4, 3 * self.__screen.height // 4,
                                                  fill="blue"))


    def start(self):
        self.__screen.canvas.bind("<Button-1>", None)
        self.__screen.clear()
        if self.on_start:
            self.on_start()

    def exit(self):
        self.__screen.window.destroy()