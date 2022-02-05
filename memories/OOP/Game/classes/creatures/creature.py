from settings import pygame
from colors import *


class BaseSprite:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, keys, world):
        pass

    def draw(self, screen, camera):
        pass


class Sprite(BaseSprite):
    def __init__(self, x, y, speed, radius=20):
        super().__init__(x, y)
        self.speed = speed
        self.radius = radius


class Creature(Sprite):
    def __init__(self, x, y, speed, hp=20, radius=20):
        super().__init__(x, y, speed, radius)
        self.hp = self.max_hp = hp

    def draw_bar(self, screen, camera, big_bar_height, bar_width, otstup=2, value=9, max_value=10, back_color=BLACK, front_color=GREEN):
        small_bar_height = big_bar_height - 2

        bot_center = [self.x, self.y - self.radius - otstup]
        big_left_up = [bot_center[0] - bar_width / 2, bot_center[1] - big_bar_height]

        small_left_up = [big_left_up[0], big_left_up[1] + 1]
        k = value / max_value
        small_width = bar_width * k

        local_big_left_up = camera.calc_coords(big_left_up)
        local_small_left_up = camera.calc_coords(small_left_up)

        pygame.draw.rect(screen, back_color, (local_big_left_up[0], local_big_left_up[1], bar_width, big_bar_height))
        pygame.draw.rect(screen, front_color, (local_small_left_up[0], local_small_left_up[1], small_width, small_bar_height))

    def draw_hp_bar(self, screen, camera):
        self.draw_bar(screen, camera, 5, self.radius * 2, 2, self.hp, self.max_hp)

    def get_damage(self, damage, world):
        raise NotImplementedError

    def die(self, *args, **kwargs):
        raise NotImplementedError

