from copy import copy

import keyboard


class KeyManager:
    def __init__(self, object_storage):
        self.__pressed_history = []
        self.__released_history = []

        self.__monitored_keys = set()
        self.__current_pressed = set()

        self.__pressed_rules = {}
        self.__released_rules = {}

        self.__storage = object_storage

    def update(self):
        for key in copy(self.__current_pressed):
            if not keyboard.is_pressed(key):
                self.release(key)

        for key in self.__monitored_keys:
            if key not in self.__current_pressed and keyboard.is_pressed(key):
                self.press(key)

    def press(self, key):
        self.__current_pressed.add(key)
        self.__pressed_history.append(key)

        for rule in self.__pressed_rules:
            if len(self.__pressed_history) >= len(rule):
                if tuple(self.__pressed_history[-len(rule):]) == rule:
                    obj = self.__pressed_rules[rule]()

                    if obj:
                        self.__storage.append(obj)

    def release(self, key):
        self.__current_pressed.remove(key)
        self.__released_history.append(key)

        for rule in self.__released_rules:
            if len(self.__released_history) > len(rule):
                if tuple(self.__released_history[-len(rule):]) == rule:
                    obj = self.__released_rules[rule]()

                    if obj:
                        self.__storage.append(obj)

    def add_press_rule(self, keys, action):
        for key in keys:
            self.__monitored_keys.add(key)

        self.__pressed_rules[keys] = action

    def add_release_rule(self, keys, action):
        for key in keys:
            self.__monitored_keys.add(key)

        self.__released_rules[keys] = action
