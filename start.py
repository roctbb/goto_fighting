from domain.game import Game
from tkinter import *

from domain.startwindow import StartWindow
from gui.screen import Screen



window = Tk()
window.attributes('-fullscreen', True)


def restart():
    screen.reset()
    game.on_end = show_menu
    game.start()


def show_menu():
    menu.draw()


screen = Screen(window)
menu = StartWindow(screen)
game = Game(screen)

menu.draw()

menu.on_start = restart

screen.window.mainloop()
