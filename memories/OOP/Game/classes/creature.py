from settings import pygame
from colors import *


class Sprite:
    def update(self, keys, world):
        pass

    def draw(self, screen, camera):
        pass


class Creature(Sprite):
    def __init__(self, x, y, speed, hp=20, radius=20):
        self.x = x
        self.y = y
        self.hp = self.max_hp = hp
        self.speed = speed
        self.radius = radius

    def draw_hp_bar(self, screen, camera):
        big_bar_height = 5
        small_bar_height = big_bar_height - 2
        bar_width = self.radius * 2

        bot_center = [self.x, self.y - self.radius - 2]
        big_left_up = [bot_center[0] - self.radius, bot_center[1] - big_bar_height]

        small_left_up = [big_left_up[0], big_left_up[1] + 1]
        k = self.hp / self.max_hp
        small_width = bar_width * k

        local_big_left_up = camera.calc_coords(big_left_up)
        local_small_left_up = camera.calc_coords(small_left_up)

        pygame.draw.rect(screen, BLACK, (local_big_left_up[0], local_big_left_up[1], bar_width, big_bar_height))
        pygame.draw.rect(screen, GREEN, (local_small_left_up[0], local_small_left_up[1], small_width, small_bar_height))

    def get_damage(self, *args, **kwargs):
        raise NotImplementedError

    def die(self, *args, **kwargs):
        raise NotImplementedError

