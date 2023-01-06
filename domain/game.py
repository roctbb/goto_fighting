from tkinter import *
import json
from domain.player import Player
from domain.skin import Skin
from domain.states import Direction
from gui.interface import Interface
from gui.screen import Screen


class Game:
    def __init__(self, screen):
        self.__screen = screen
        self.__player1 = None
        self.__player2 = None
        self.__interface = None
        self.__balls = []

    def start(self):
        with open('assets/skins/roctbb/skin.json') as file:
            data = json.load(file)

        skin1 = Skin(data)
        skin2 = Skin(data)

        self.__screen.window.update()

        self.__player1 = Player(Direction.RIGHT, self.__screen, skin1)
        self.__player2 = Player(Direction.LEFT, self.__screen, skin2)

        self.__interface = Interface(self.__player1, self.__player2, self.__screen)

        self.__balls = []

        self.__screen.window.bind("<KeyPress>", self.__key_press_handler)
        self.__screen.window.bind("<KeyRelease>", self.__key_release_handler)
        self.__screen.window.after(20, self.update)
        mainloop()

    def __key_press_handler(self, event):
        if event.char == 'w':
            self.__player1.jump()
        if event.char == 'a':
            self.__player1.left()
        if event.char == 's':
            self.__player1.sit()
        if event.char == 'd':
            self.__player1.right()
        if event.char == 'q':
            self.__player1.hit_leg()
        if event.char == 'e':
            self.__player1.hit_hand()
        if event.char == 'f':
            ball = self.__player1.shot()
            self.__balls.append(ball)

        if event.char == 'i':
            self.__player2.jump()
        if event.char == 'l':
            self.__player2.right()
        if event.char == 'k':
            self.__player2.sit()
        if event.char == 'j':
            self.__player2.left()
        if event.char == 'u':
            self.__player2.hit_leg()
        if event.char == 'o':
            self.__player2.hit_hand()

    def __key_release_handler(self, event):
        if event.char == 's':
            self.__player1.stand()
        if event.char == 'k':
            self.__player2.stand()
        if event.char == 'a':
            self.__player1.stop()
        if event.char == 'd':
            self.__player1.stop()
        if event.char == 'l':
            self.__player2.stop()
        if event.char == 'j':
            self.__player2.stop()

    def update(self):
        self.__player1.update()
        self.__player2.update()

        alive_balls = []
        for ball in self.__balls:
            ball.update()
            if not ball.is_dead:
                alive_balls.append(ball)
        self.__balls = alive_balls

        if self.__player1.intersects_with(self.__player2):
            if self.__player1.is_attacking:
                self.__player2.make_damage(self.__player1.attack_power)
                self.__player1.cooldown()

        if self.__player2.intersects_with(self.__player1):
            if self.__player2.is_attacking:
                self.__player1.make_damage(self.__player2.attack_power)
                self.__player2.cooldown()

        if self.__player1.x < self.__player2.x and self.__player1.direction == Direction.LEFT:
            self.__player1.flip()

        if self.__player1.x > self.__player2.x and self.__player1.direction == Direction.RIGHT:
            self.__player1.flip()

        if self.__player2.x < self.__player1.x and self.__player2.direction == Direction.LEFT:
            self.__player2.flip()

        if self.__player2.x > self.__player1.x and self.__player2.direction == Direction.RIGHT:
            self.__player2.flip()

        self.__screen.window.after(20, self.update)
        self.draw()

    def draw(self):
        self.__screen.clear()
        self.__player1.draw()
        self.__player2.draw()
        self.__interface.draw()

        for ball in self.__balls:
            ball.draw()
