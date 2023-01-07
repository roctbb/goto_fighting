from tkinter import *
import json

import pygame

from domain.player import Player
from domain.room import Room
from domain.skin import Skin
from gui.states import Direction
from gui.common import asset_path
from gui.interface import Interface
from gui.keymanager import KeyManager


class Game:

    def __init__(self, screen):
        self.__screen = screen
        pygame.mixer.init()
        self.__clear()

        self.__screen.window.bind("<KeyPress>",
                                  lambda event: self.__pressed(event.char))
        self.__screen.window.bind("<KeyRelease>",
                                  lambda event: self.__released(event.char))
        self.__screen.window.bind('<Escape>', lambda event: self.pause())

    def __clear(self):
        self.__player1 = None
        self.__player2 = None
        self.__interface = None
        self.__balls = []
        self.__key_manager1 = None
        self.__key_manager2 = None
        self.__room = None
        self.on_end = None
        self.__closed = False
        self.__ended = False

    def pause(self):
        self.__interface.pause()
        if self.__key_manager1.enabled:
            self.__key_manager1.disable()
            self.__key_manager2.disable()
        else:
            self.__key_manager1.enable()
            self.__key_manager2.enable()

    def __init_rules(self):

        # player 1
        self.__key_manager1.add_press_rule(('w',), self.__player1.jump)
        self.__key_manager1.add_press_rule(('s',), self.__player1.sit)
        self.__key_manager1.add_press_rule(('a',), self.__player1.left)
        self.__key_manager1.add_press_rule(('d',), self.__player1.right)

        self.__key_manager1.add_press_rule(('e',), self.__player1.hit_hand)
        self.__key_manager1.add_press_rule(('q',), self.__player1.hit_leg)

        self.__key_manager1.add_press_rule(('f',), self.__player1.block)
        self.__key_manager1.add_press_rule(('e', 'e', 'x', 'd'), self.__player1.shot)
        self.__key_manager1.add_press_rule(('d', 'd', 'd'), self.__player1.fly_right)
        self.__key_manager1.add_press_rule(('a', 'a', 'a'), self.__player1.fly_left)
        self.__key_manager1.add_press_rule(('s', 's', 'w', 'w'), self.__player1.super_jump)

        self.__key_manager1.add_release_rule(('s',), self.__player1.stand)
        self.__key_manager1.add_release_rule(('d',), self.__player1.stop)
        self.__key_manager1.add_release_rule(('a',), self.__player1.stop)
        self.__key_manager1.add_release_rule(('f',), self.__player1.unblock)

        # player 2
        self.__key_manager2.add_press_rule(('i',), self.__player2.jump)
        self.__key_manager2.add_press_rule(('k',), self.__player2.sit)
        self.__key_manager2.add_press_rule(('j',), self.__player2.left)
        self.__key_manager2.add_press_rule(('l',), self.__player2.right)

        self.__key_manager2.add_press_rule(('u',), self.__player2.hit_hand)
        self.__key_manager2.add_press_rule(('o',), self.__player2.hit_leg)

        self.__key_manager2.add_press_rule(('h',), self.__player2.block)
        self.__key_manager2.add_press_rule(('o', 'o', ',', 'l'), self.__player2.shot)
        self.__key_manager2.add_press_rule(('j', 'j', 'j'), self.__player2.fly_left)
        self.__key_manager2.add_press_rule(('l', 'l', 'l'), self.__player2.fly_right)
        self.__key_manager2.add_press_rule(('k', 'k', 'i', 'i'), self.__player2.super_jump)

        self.__key_manager2.add_release_rule(('k',), self.__player2.stand)
        self.__key_manager2.add_release_rule(('j',), self.__player2.stop)
        self.__key_manager2.add_release_rule(('l',), self.__player2.stop)
        self.__key_manager2.add_release_rule(('h',), self.__player2.unblock)

    def __pressed(self, key):
        if self.__key_manager1 and self.__key_manager2:
            self.__key_manager1.press(key)
            self.__key_manager2.press(key)

    def __released(self, key):
        if self.__key_manager1 and self.__key_manager2:
            self.__key_manager1.release(key)
            self.__key_manager2.release(key)

    @property
    def balls(self):
        return self.__balls

    def start(self):
        print("starting")

        if self.__player1:
            self.__clear()

        self.__key_manager1 = KeyManager(self.__balls)
        self.__key_manager2 = KeyManager(self.__balls)

        with open('assets/skins/roctbb/skin.json') as file:
            data1 = json.load(file)
        with open('assets/skins/tvorog/skin.json') as file:
            data2 = json.load(file)

        with open('assets/rooms/room1/room.json') as file:
            room_description = json.load(file)

        skin1 = Skin(data1)
        skin2 = Skin(data2)

        self.__player1 = Player(Direction.RIGHT, self.__screen, skin1)
        self.__player2 = Player(Direction.LEFT, self.__screen, skin2)
        self.__room = Room(room_description, self.__screen)
        self.music()

        self.__interface = Interface(self.__player1, self.__player2, self.__screen)

        self.__init_rules()

        self.__screen.window.after(20, self.update)

    def update(self):
        if not self.__closed:
            if self.__screen.frames == 90:
                self.__player1.fight()
                self.__player2.fight()

            if self.__player1.hp == 0:
                self.__player1.loss()

                if self.__player2.hp != 0:
                    self.__player2.win()

            if self.__player2.hp == 0:
                self.__player2.loss()

                if self.__player1 != 0:
                    self.__player1.win()

            self.__player1.update()
            self.__player2.update()

            for ball in self.__balls[:]:
                ball.update()
                if ball.is_dead:
                    self.__balls.remove(ball)

            if self.__player1.intersects_with(self.__player2):
                if self.__player1.get_intersection_with(self.__player2) > self.__player1.width / 3:
                    if self.__player1.is_attacking:
                        self.__player2.receive_attack(self.__player1.current_attack)
                        self.__player1.cooldown()

            if self.__player2.get_intersection_with(self.__player1) > self.__player2.width / 3:
                if self.__player2.is_attacking:
                    if self.__player2.is_attacking:
                        self.__player1.receive_attack(self.__player2.current_attack)
                        self.__player2.cooldown()

            for ball in self.__balls:
                if self.__player2.get_intersection_with(ball) > self.__player2.width / 2:
                    print("ball intersects with player 2")
                    self.__player2.receive_ball(ball)
                    ball.die()
                if self.__player1.get_intersection_with(ball) > self.__player1.width / 2:
                    print("ball intersects with player 1")
                    self.__player1.receive_ball(ball)
                    ball.die()

            if self.__player1.x < self.__player2.x and self.__player1.direction == Direction.LEFT:
                self.__player1.flip()

            if self.__player1.x > self.__player2.x and self.__player1.direction == Direction.RIGHT:
                self.__player1.flip()

            if self.__player2.x < self.__player1.x and self.__player2.direction == Direction.LEFT:
                self.__player2.flip()

            if self.__player2.x > self.__player1.x and self.__player2.direction == Direction.RIGHT:
                self.__player2.flip()

            if self.__player1.hp == 0 or self.__player2.hp == 0 or self.__interface.time_left <= 0:
                if not self.__ended:
                    print("should close")
                    self.__ended = True
                    self.__screen.window.after(3000, self.close)

            self.__screen.window.after(20, self.update)
            self.draw()

    def close(self):
        print("closing")
        self.__closed = True
        if self.on_end:
            self.__screen.window.after(200, self.on_end)

    def draw(self):
        self.__screen.clear()
        self.__room.draw()
        self.__player1.draw()
        self.__player2.draw()
        self.__interface.draw()

        for ball in self.__balls:
            ball.draw()

    def music(self):
        pygame.mixer.music.load(asset_path('/music/1.ogg'))
        pygame.mixer.music.play(-1)
