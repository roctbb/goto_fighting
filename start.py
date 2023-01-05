from tkinter import *

from domain.player import Player

def key_handler(event):
    if event.char == 'w':
        player1.jump()
    if event.char == 'a':
        player1.backward()
    if event.char == 's':
        player1.sit_down()
    if event.char == 'd':
        player1.forward()

    if event.char == 'i':
        player2.jump()
    if event.char == 'l':
        player2.forward()
    if event.char == 'k':
        player2.sit_down()
    if event.char == 'j':
        player2.backward()

def draw_all():
    player1.draw(canvas)
    player2.draw(canvas)
    window.after(20, draw_all)

window = Tk()
canvas = Canvas(window, width=640, height=640)
canvas.pack()

player1 = Player(50, 50, 'right', None)
player2 = Player(150, 50, 'left', None)

window.bind("<KeyPress>", key_handler)
window.after(20, draw_all)
mainloop()