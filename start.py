from tkinter import *

from domain.player import Player
from gui.screen import Screen


def key_handler(event):
    if event.char == 'w':
        player1.jump()
    if event.char == 'a':
        player1.left()
    if event.char == 's':
        player1.sit_down()
    if event.char == 'd':
        player1.right()

    if event.char == 'i':
        player2.jump()
    if event.char == 'l':
        player2.right()
    if event.char == 'k':
        player2.sit_down()
    if event.char == 'j':
        player2.left()


def draw_all():
    screen.clear()
    player1.draw()
    player2.draw()
    window.after(20, draw_all)



window = Tk()
screen = Screen(window)

player1 = Player(50, 50, 'right', screen, None)
player2 = Player(150, 50, 'left', screen, None)

window.bind("<KeyPress>", key_handler)
window.after(20, draw_all)
mainloop()
