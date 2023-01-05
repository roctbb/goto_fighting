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
    if event.char == 'q':
        player1.hit_leg()
    if event.char == 'e':
        player1.hit_hand()

    if event.char == 'i':
        player2.jump()
    if event.char == 'l':
        player2.right()
    if event.char == 'k':
        player2.sit_down()
    if event.char == 'j':
        player2.left()
    if event.char == 'u':
        player2.hit_leg()
    if event.char == 'o':
        player2.hit_hand()


def draw_all():
    screen.clear()
    player1.draw()
    player2.draw()

    if player1.intersects_with(player2):
        print("Пересечение")

        # TODO Если player1 в состоянии атаки, нанести второму игроку урон в размере силы атаки первого игрока

    window.after(20, draw_all)


window = Tk()
screen = Screen(window)

player1 = Player(200, 250, 'right', screen, None)
player2 = Player(350, 250, 'left', screen, None)

window.bind("<KeyPress>", key_handler)
window.after(20, draw_all)
mainloop()
