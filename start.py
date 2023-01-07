from domain.game import Game
from tkinter import *

from gui.screen import Screen

window = Tk()
window.attributes('-fullscreen', True)


def restart():
    screen.reset()
    game.start()


screen = Screen(window)

game = Game(screen)
game.on_end = restart
game.start()

screen.window.mainloop()
