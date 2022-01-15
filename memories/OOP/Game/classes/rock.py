from classes.creature import Sprite
from colors import *
import random
from tools.math_ops import *
from settings import pygame


class Rock(Sprite):
    def __init__(self, x, y, radius=7):
        self.x = x
        self.y = y
        self.radius = radius

    def update(self, keys, world):
        pass

    def draw(self, screen, camera):
        pygame.draw.circle(screen, BLACK, camera.calc_coords([self.x, self.y]), self.radius)

    @classmethod
    def generate_random(cls):
        return cls(random.randint(-4000, 4000), random.randint(-4000, 4000), radius=random.randint(5, 10))

    @classmethod
    def generate_many_rocks(cls, n=300):
        return [cls.generate_random() for _ in range(n)]
