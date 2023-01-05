from tkinter import *

from domain.player import Player

window = Tk()
canvas = Canvas(window, width=640, height=640)
canvas.pack()

player1 = Player(50, 50, 'right', None)
player2 = Player(150, 50, 'left', None)

player1.draw(canvas)
player2.draw(canvas)

mainloop()