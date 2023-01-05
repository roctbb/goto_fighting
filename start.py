from tkinter import *

from domain.player import Player
from gui.screen import Screen


def key_press_handler(event):
    if event.char == 'w':
        player1.jump()
    if event.char == 'a':
        player1.left()
    if event.char == 's':
        player1.sit()
    if event.char == 'd':
        player1.right()

    if event.char == 'i':
        player2.jump()
    if event.char == 'l':
        player2.right()
    if event.char == 'k':
        player2.sit()
    if event.char == 'j':
        player2.left()


def key_release_handler(event):
    if event.char == 's':
        player1.stand()
    if event.char == 'k':
        player2.stand()


def draw_all():
    screen.clear()
    player1.draw()
    player2.draw()
    window.after(20, draw_all)


window = Tk()
screen = Screen(window)

player1 = Player(200, 250, 'right', screen, None)
player2 = Player(350, 250, 'left', screen, None)

window.bind("<KeyPress>", key_press_handler)
window.bind("<KeyRelease>", key_release_handler)
window.after(20, draw_all)
mainloop()
