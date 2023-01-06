from tkinter import NW

from gui.animation import Animation
from gui.screen import Screen


class Room:
    def __init__(self, room_description, screen: Screen):
        self.__background = Animation(room_description["images"], (screen.width, screen.height))
        self.__screen = screen

    def draw(self):
        rect = self.__screen.canvas.create_image(0, 0,
                                                 image=self.__background.get_image(), anchor=NW)
        self.__screen.add_object(rect)
