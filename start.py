from tkinter import *
import json
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
        if player1.is_attacking:
            player2.make_damage(player1.attack_power)


    if player2.intersects_with(player1):
        print("Пересечение")
        if player2.is_attacking:
            player1.make_damage(player2.attack_power)



    window.after(20, draw_all)

    if player1.x < player2.x and player1.direction == Direction.LEFT:
        player1.flip()

    if player1.x > player2.x and player1.direction == Direction.RIGHT:
        player1.flip()

    if player2.x < player1.x and player2.direction == Direction.LEFT:
        player2.flip()

    if player2.x > player1.x and player2.direction == Direction.RIGHT:
        player2.flip()

window = Tk()
window.attributes('-fullscreen', True)
screen = Screen(window)

with open('assets/skins/roctbb/skin.json') as file:
    data = json.load(file)
skin1 = Skin(data)
skin2 = Skin(data)

player1 = Player(200, 150, Direction.RIGHT, screen, skin1)
player2 = Player(350, 150, Direction.LEFT, screen, skin2)

window.bind("<KeyPress>", key_press_handler)
window.bind("<KeyRelease>", key_release_handler)
window.after(20, draw_all)
mainloop()
