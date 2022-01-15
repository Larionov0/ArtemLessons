from classes.enemy import Enemy
from colors import *
from tools.math_ops import *


class Rabbit(Enemy):
    def __init__(self, x, y, speed, hp=20, vision_range=200, radius=10, color=GREEN):
        super().__init__(x, y, speed, hp, vision_range, radius, color)

    def update(self, keys, world):
        hero = world.hero
        if distance([self.x, self.y], [hero.x, hero.y]) < self.vision_range:
            self.patrol_vector_time -= 10
            vector = [hero.x - self.x, hero.y - self.y]
            vector = [-vector[0], -vector[1]]
            vector_length = get_vector_length(vector)

            mini_vector = [vector[0] * self.speed / vector_length, vector[1] * self.speed / vector_length]

            self.x += mini_vector[0]
            self.y += mini_vector[1]
        else:
            self.patrol()
