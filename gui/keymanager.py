class KeyManager:
    def __init__(self, object_storage):
        self.__pressed = []
        self.__released = []

        self.__pressed_rules = {}
        self.__released_rules = {}

        self.__storage = object_storage

    def press(self, key):
        self.__pressed.append(key)

        for rule in self.__pressed_rules:
            if len(self.__pressed) >= len(rule):
                if tuple(self.__pressed[-len(rule):]) == rule:
                    obj = self.__pressed_rules[rule]()

                    if obj:
                        self.__storage.append(obj)

    def release(self, key):
        self.__released.append(key)

        for rule in self.__released_rules:
            if len(self.__released) > len(rule):
                if tuple(self.__released[-len(rule):]) == rule:
                    obj = self.__released_rules[rule]()

                    if obj:
                        self.__storage.append(obj)

    def add_press_rule(self, keys, action):
        self.__pressed_rules[keys] = action

    def add_release_rule(self, keys, action):
        self.__released_rules[keys] = action
