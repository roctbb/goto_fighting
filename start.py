from domain.game import Game
from tkinter import *

from gui.screen import Screen
from gui.mainmenu import MainMenu

window = Tk()
window.attributes('-fullscreen', True)

screen = Screen(window)

game = MainMenu(screen)

game.draw_main()
