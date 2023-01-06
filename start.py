from domain.game import Game
from tkinter import *

from gui.screen import Screen

window = Tk()
window.attributes('-fullscreen', True)

screen = Screen(window)

game = Game(screen)

game.start()
