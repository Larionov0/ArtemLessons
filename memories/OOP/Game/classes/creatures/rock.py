from classes.creatures.creature import Sprite
from colors import *
import random
from settings import pygame, WORLD_WIDTH, WORLD_HEIGHT


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
        return cls(random.randint(0, WORLD_WIDTH), random.randint(0, WORLD_HEIGHT), radius=random.randint(5, 10))

    @classmethod
    def generate_many_rocks(cls, n=200):
        return [cls.generate_random() for _ in range(n)]
