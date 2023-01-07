from domain.game import Game
from tkinter import *

from domain.startwindow import StartWindow
from gui.screen import Screen



window = Tk()
window.attributes('-fullscreen', True)


def restart():
    screen.reset()
    game.start()


screen = Screen(window)
menu = StartWindow(screen)
game = Game(screen)
game.on_end = restart

menu.draw()

menu.on_start = restart

screen.window.mainloop()
