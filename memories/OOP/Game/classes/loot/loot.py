from classes.creature import Sprite
from classes.loot.loot_types import *
import colors
import pygame
import time
import random


class Loot(Sprite):
    COLOR_TRANSLATE = {
        GOLD: colors.GOLD,
        BULLETS: colors.BLACK
    }

    def __init__(self, x, y, type, amount, vector, speed=10, a=-2, radius=10):
        super().__init__(x, y, speed, radius)
        self.type = type
        self.amount = amount
        self.color = self.COLOR_TRANSLATE[type]
        self.a = a
        self.vector = vector

    @classmethod
    def spawn_in_random_dir(cls, x, y, type, amount):
        return cls(x, y, type, amount,
                   vector=[random.randint(-10, 10) / 10, random.randint(-10, 10) / 10],
                   speed=random.randint(8, 14),
                   a=random.randint(1, 10) / 10)

    def destroy(self, world):
        world.loot.remove(self)

    def calc_current_speed(self):
        self.speed -= self.a
        if self.speed < 0:
            self.speed = 0
        return self.speed

    def calc_current_vector(self):
        speed = self.calc_current_speed()
        d = (self.vector[0] ** 2 + self.vector[1] ** 2) ** 0.5
        k = speed / d if d != 0 else 0
        return [self.vector[0] * k, self.vector[1] * k]

    def update(self, keys, world):
        if self.speed != 0:
            vector = self.calc_current_vector()
            self.x += vector[0]
            self.y += vector[1]

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.calc_coords([self.x, self.y]), self.radius)
