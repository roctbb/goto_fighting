import json
from tkinter import *

from domain.player import Player
from domain.skin import Skin
from domain.states import Direction
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
    if event.char == 'q':
        player1.hit_leg()
    if event.char == 'e':
        player1.hit_hand()

    if event.char == 'i':
        player2.jump()
    if event.char == 'l':
        player2.right()
    if event.char == 'k':
        player2.sit()
    if event.char == 'j':
        player2.left()
    if event.char == 'u':
        player2.hit_leg()
    if event.char == 'o':
        player2.hit_hand()


def key_release_handler(event):
    if event.char == 's':
        player1.stand()
    if event.char == 'k':
        player2.stand()
    if event.char == 'a':
        player1.stop()
    if event.char == 'd':
        player1.stop()
    if event.char == 'l':
        player2.stop()
    if event.char == 'j':
        player2.stop()


def draw_all():
    screen.clear()
    player1.draw()
    player2.draw()

    # TODO: зеркалить игроков если нужно

    if player1.intersects_with(player2):
        print("Пересечение")

        # TODO Если player1 в состоянии атаки, нанести второму игроку урон в размере силы атаки первого игрока

    window.after(20, draw_all)


window = Tk()
screen = Screen(window)

with open('assets/skins/roctbb/skin.json') as file:
    data = json.load(file)
skin = Skin(data)

player1 = Player(200, 250, Direction.RIGHT, screen, skin)
player2 = Player(350, 250, Direction.LEFT, screen, skin)

window.bind("<KeyPress>", key_press_handler)
window.bind("<KeyRelease>", key_release_handler)
window.after(20, draw_all)
mainloop()
