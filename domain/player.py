from domain.flying_ball import Ball
from domain.object import Object
from domain.skin import Skin
from gui.states import MoveState, HitState, Direction
from gui.screen import Screen
from tkinter import NW
from domain.attack import Attack


class Player(Object):
    LEG_POWER = 15
    HAND_POWER = 10

    JUMP_SPEED = 50

    HIT_TIME = 10
    COOLDOWN = 5
    SHOT_COOLDOWN = 500

    HP = 1000

    DAMAGE_RULES = {
        # противник противник мы блок
        # ------------------------ STAND -----------------------------
        (MoveState.JUMP, HitState.HAND, MoveState.STAND, True): 0,
        (MoveState.JUMP, HitState.HAND, MoveState.STAND, False): 0,
        (MoveState.JUMP, HitState.LEG, MoveState.STAND, True): 0.5,
        (MoveState.JUMP, HitState.LEG, MoveState.STAND, False): 1.5,

        (MoveState.STAND, HitState.HAND, MoveState.STAND, True): 0.3,
        (MoveState.STAND, HitState.HAND, MoveState.STAND, False): 1,
        (MoveState.STAND, HitState.LEG, MoveState.STAND, True): 0.3,
        (MoveState.STAND, HitState.LEG, MoveState.STAND, False): 1,

        (MoveState.SIT, HitState.HAND, MoveState.STAND, True): 1,
        (MoveState.SIT, HitState.HAND, MoveState.STAND, False): 1,
        (MoveState.SIT, HitState.LEG, MoveState.STAND, True): 1,
        (MoveState.SIT, HitState.LEG, MoveState.STAND, False): 1,

        # ------------------------ SIT -----------------------------

        (MoveState.JUMP, HitState.HAND, MoveState.SIT, True): 0,
        (MoveState.JUMP, HitState.HAND, MoveState.SIT, False): 0,
        (MoveState.JUMP, HitState.LEG, MoveState.SIT, True): 0.5,
        (MoveState.JUMP, HitState.LEG, MoveState.SIT, False): 1.5,

        (MoveState.STAND, HitState.HAND, MoveState.SIT, True): 0,
        (MoveState.STAND, HitState.HAND, MoveState.SIT, False): 0,
        (MoveState.STAND, HitState.LEG, MoveState.SIT, True): 0.5,
        (MoveState.STAND, HitState.LEG, MoveState.SIT, False): 1.5,

        (MoveState.SIT, HitState.HAND, MoveState.SIT, True): 0.3,
        (MoveState.SIT, HitState.HAND, MoveState.SIT, False): 1,
        (MoveState.SIT, HitState.LEG, MoveState.SIT, True): 0.5,
        (MoveState.SIT, HitState.LEG, MoveState.SIT, False): 1.5,

        # ----------------------- JUMP --------------------------

        (MoveState.JUMP, HitState.HAND, MoveState.JUMP, True): 0.3,
        (MoveState.JUMP, HitState.HAND, MoveState.JUMP, False): 1,
        (MoveState.JUMP, HitState.LEG, MoveState.JUMP, True): 0.3,
        (MoveState.JUMP, HitState.LEG, MoveState.JUMP, False): 1,

        (MoveState.STAND, HitState.HAND, MoveState.JUMP, True): 0.3,
        (MoveState.STAND, HitState.HAND, MoveState.JUMP, False): 1,
        (MoveState.STAND, HitState.LEG, MoveState.JUMP, True): 0.3,
        (MoveState.STAND, HitState.LEG, MoveState.JUMP, False): 1,

        (MoveState.SIT, HitState.HAND, MoveState.JUMP, True): 0,
        (MoveState.SIT, HitState.HAND, MoveState.JUMP, False): 0,
        (MoveState.SIT, HitState.LEG, MoveState.JUMP, True): 0,
        (MoveState.SIT, HitState.LEG, MoveState.JUMP, False): 0,

    }

    def __init__(self, direction, screen: Screen, skin: Skin):
        if direction == Direction.RIGHT:
            x, y = skin.width // 2, screen.height - skin.height
        else:
            x, y = screen.width - int(skin.width * 1.5), screen.height - skin.height

        super().__init__(x, y, skin.width, skin.height, direction, screen)

        self.__initial_height = skin.height
        self.__hp = self.HP
        self.__skin = skin
        self.__speed = 10
        self.__move_state = MoveState.START
        self.__hit_state = HitState.NO
        self.__hit_timer = 0
        self.__cooldown_timer = 0
        self.__jump_speed = 0
        self.__move_speed = 0
        self.__shot_timer = 0

    @property
    def hp(self):
        return self.__hp

    @property
    def name(self):
        return self.__skin.name

    @property
    def direction(self):
        return self._direction

    @property
    def shot_ready_percent(self):
        return int(100 - self.__shot_timer * 100 / self.SHOT_COOLDOWN)

    def make_damage(self, amount):
        self.__hp = max(0, self.__hp - amount)

    def receive_attack(self, attack: Attack):
        coef = self.DAMAGE_RULES.get(
            (attack.move_state, attack.hit_state, self.__move_state, self.__hit_state == HitState.BLOCK))

        if coef:
            self.make_damage(int(attack.power * coef))

    def receive_ball(self, ball: Ball):
        self.make_damage(ball.attack_power)
        self.__skin.play_sound("hit_to_player")

    # навыки
    def block(self):
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        self.__hit_timer = 20
        self.__hit_state = HitState.BLOCK

    def unblock(self):
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        self.__hit_timer = 0
        self.__hit_state = HitState.NO

    def hit_hand(self):
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        self.__hit_state = HitState.HAND
        self.__hit_timer = self.HIT_TIME
        self.__skin.play_sound("hit")

    def hit_leg(self):
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        self.__hit_state = HitState.LEG
        self.__hit_timer = self.HIT_TIME
        self.__skin.play_sound("hit")

    def shot(self):
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        if self.__shot_timer != 0:
            return

        self.__hit_state = HitState.SHOT
        self.__hit_timer = self.HIT_TIME
        self.__shot_timer = self.SHOT_COOLDOWN

        self.__skin.play_sound("shot")

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

    def __play_audio_with_delay(self, sound):
        if self.direction == Direction.LEFT:
            self._screen.window.after(2000, lambda: self.__skin.play_sound(sound))
        else:
            self.__skin.play_sound(sound)

    @property
    def attack_power(self):
        if self.__cooldown_timer == 0:
            if self.__hit_state == HitState.LEG:
                return self.LEG_POWER
            if self.__hit_state == HitState.HAND:
                return self.HAND_POWER
        return 0

    def cooldown(self):
        if self.__cooldown_timer == 0:
            self.__cooldown_timer = self.COOLDOWN

    def sit(self):
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        if self.__move_state == MoveState.STAND:
            print("sitting")
            self.__move_state = MoveState.SIT
            self._height = self.__initial_height // 2
            self.move_by(0, self._height)

    def stand(self):
        print("standing")
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        if self.__move_state == MoveState.SIT:
            self._height = self.__initial_height
            self.__move_state = MoveState.STAND
            self.move_by(0, self._height)

    def jump(self):
        self.__skin.play_sound("jump")
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        if self.__jump_speed == 0:
            self.stand()

            self.__jump_speed = -self.JUMP_SPEED
            self.move_by(0, self.__jump_speed)
            self.__move_state = MoveState.JUMP

    def super_jump(self):
        print("superjump")
        if self.y > 0:
            self.__jump_speed = -self.JUMP_SPEED * 2

    def fly_left(self):
        if self.__move_state in [MoveState.JUMP, MoveState.SIT]:
            self.__move_speed = -50

    def fly_right(self):
        if self.__move_state in [MoveState.JUMP, MoveState.SIT]:
            self.__move_speed = 50

    def right(self):
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        self.__move_speed = 10

    def left(self):
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        self.__move_speed = -10

    def stop(self):
        if self.__move_state in [MoveState.START, MoveState.WIN, MoveState.LOSS]:
            return

        self.__move_speed = 0

    def fight(self):
        self.__move_state = MoveState.STAND
        self.__play_audio_with_delay('start')

    def win(self):
        if self.__move_state != MoveState.WIN:
            self.__move_state = MoveState.WIN
            self.__hit_state = HitState.NO
            self.__play_audio_with_delay("win")

    def loss(self):
        if self.__move_state != MoveState.LOSS:
            self.__move_state = MoveState.LOSS
            self.__hit_state = HitState.NO
            self.__play_audio_with_delay("loss")
            self._height = self.__initial_height // 2
            self.move_by(0, self._height)

    def update(self):
        if self.__cooldown_timer > 0:
            self.__cooldown_timer -= 1

        if self.__shot_timer != 0:
            self.__shot_timer -= 1

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
