from domain.flying_ball import Ball
from domain.object import Object
from domain.skin import Skin
from domain.states import MoveState, HitState, Direction
from gui.screen import Screen
from tkinter import NW
from domain.attack import Attack


class Player(Object):
    LEG_POWER = 15
    HAND_POWER = 10
    SHOT_POWER = 20

    JUMP_SPEED = 50

    HIT_TIME = 5
    COOLDOWN = 5

    def __init__(self, direction, screen: Screen, skin: Skin):
        if direction == Direction.RIGHT:
            x, y = skin.width // 2, screen.height - skin.height
        else:
            x, y = screen.width - int(skin.width * 1.5), screen.height - skin.height

        super().__init__(x, y, skin.width, skin.height, direction, screen)

        self.__initial_height = skin.height
        self.__hp = 100
        self.__skin = skin
        self.__speed = 10
        self.__move_state = MoveState.START
        self.__hit_state = HitState.NO
        self.__hit_timer = 0
        self.__cooldown_timer = 0
        self.__jump_speed = 0
        self.__move_speed = 0

    @property
    def hp(self):
        return self.__hp

    @property
    def direction(self):
        return self._direction

    def make_damage(self, amount):
        self.__hp = max(0, self.__hp - amount)

    def receive_attack(self, attack: Attack):
        if self.__move_state == MoveState.SIT and attack.move_state == MoveState.STAND:
            return
        if self.__move_state == MoveState.JUMP and attack.hit_state == HitState.LEG:
            return
        if self.__move_state == MoveState.SIT and attack.hit_state == HitState.HAND:
            return
        if self.__hit_state == HitState.BLOCK:
            if attack.hit_state == HitState.HAND:
                self.make_damage(int(attack.power * 0.2))
            if attack.hit_state == HitState.LEG:
                self.make_damage(int(attack.power * 0.3))
                print(attack.power)
            return
        self.make_damage(attack.power)

    # навыки
    def block(self):
        if self.__move_state == MoveState.START:
            return

        self.__hit_timer = 20
        self.__hit_state = HitState.BLOCK

    def unblock(self):
        if self.__move_state == MoveState.START:
            return

        self.__hit_timer = 0
        self.__hit_state = HitState.NO

    def hit_hand(self):
        if self.__move_state == MoveState.START:
            return

        self.__hit_state = HitState.HAND
        self.__hit_timer = self.HIT_TIME

    def hit_leg(self):
        if self.__move_state == MoveState.START:
            return

        self.__hit_state = HitState.LEG
        self.__hit_timer = self.HIT_TIME

    def shot(self):
        if self.__move_state == MoveState.START:
            return

        self.__hit_state = HitState.SHOT
        self.__hit_timer = self.HIT_TIME

        if self.direction == Direction.LEFT:
            return Ball(self.x - Ball.WIDTH, self.y + (self.height - Ball.HEIGHT) / 8, self.direction,
                        self.__skin.bullet_animation, self._screen)
        else:
            return Ball(self.x + self.width, self.y + (self.height - Ball.HEIGHT) / 8, self.direction,
                        self.__skin.bullet_animation, self._screen)

    @property
    def is_attacking(self):
        if self.__hit_state in [HitState.LEG, HitState.HAND]:
            return True
        return False

    @property
    def current_attack(self):
        if not self.is_attacking:
            return None
        return Attack(self.__move_state, self.__hit_state, self.attack_power)

    @property
    def attack_power(self):
        if self.__cooldown_timer == 0:
            if self.__hit_state == HitState.LEG:
                return self.LEG_POWER
            if self.__hit_state == HitState.HAND:
                return self.HAND_POWER
            if self.__hit_state == HitState.SHOT:
                return self.SHOT_POWER
        return 0

    def cooldown(self):
        if self.__cooldown_timer == 0:
            self.__cooldown_timer = self.COOLDOWN

    def sit(self):
        if self.__move_state == MoveState.START:
            return

        if self.__move_state == MoveState.STAND:
            print("sitting")
            self.__move_state = MoveState.SIT
            self._height = self.__initial_height // 2
            self.move_by(0, self._height)

    def stand(self):
        print("standing")
        if self.__move_state == MoveState.START:
            return

        if self.__move_state == MoveState.SIT:
            self._height = self.__initial_height
            self.__move_state = MoveState.STAND
            self.move_by(0, self._height)

    def jump(self):
        if self.__move_state == MoveState.START:
            return

        if self.__jump_speed == 0:
            self.stand()

            self.__jump_speed = -self.JUMP_SPEED
            self.move_by(0, self.__jump_speed)
            self.__move_state = MoveState.JUMP

    def fly(self):
        if self.__move_state == MoveState.JUMP:
            if self.direction == Direction.LEFT:
                self.__move_speed = -50
            if self.direction == Direction.RIGHT:
                self.__move_speed = 50

    def right(self):
        if self.__move_state == MoveState.START:
            return

        self.__move_speed = 10

    def left(self):
        if self.__move_state == MoveState.START:
            return

        self.__move_speed = -10

    def stop(self):
        if self.__move_state == MoveState.START:
            return

        self.__move_speed = 0

    def fight(self):
        self.__move_state = MoveState.STAND

    def update(self):
        if self.__cooldown_timer > 0:
            self.__cooldown_timer -= 1

        if self.__hit_timer == 0 and self.__hit_state != HitState.BLOCK:
            self.__hit_state = HitState.NO
        else:
            self.__hit_timer -= 1

        if self.y + self.height == self._screen.height:
            self.__jump_speed = 0
            if self.__move_state == MoveState.JUMP:
                self.__move_state = MoveState.STAND
        else:
            self.move_by(0, self.__jump_speed)
            self.__jump_speed += self.GRAVITY

        self.move_by(self.__move_speed, 0)

    def draw(self):
        rect = self._screen.canvas.create_image(self.x, self.y,
                                                image=self.__skin.get_image(self.direction, self.__move_state,
                                                                            self.__hit_state), anchor=NW)
        self._screen.add_object(rect)

