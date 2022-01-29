from classes.creature import Sprite
from tools.math_ops import *
from colors import *
from settings import pygame
import time


class Bullet(Sprite):
    def __init__(self, x, y, speed, vector, damage=5, color=BLACK, radius=3):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.radius = radius
        self.vector = vector
        self.damage = damage
        self.start_time = time.time()
        self.life_time = 8

    @classmethod
    def spawn(cls, x, y, start_vector, speed, damage=None):
        length = get_vector_length(start_vector)
        return cls(x, y, speed, [start_vector[0] * speed / length, start_vector[1] * speed / length], damage)

    def update(self, keys, world):
        if time.time() - self.start_time > self.life_time:
            world.bullets.remove(self)

        x, y = self.x, self.y
        x += self.vector[0]
        y += self.vector[1]

        for rock in world.rocks:
            if distance([x, y], [rock.x, rock.y]) < rock.radius + self.radius:
                try:
                    world.bullets.remove(self)
                except:
                    pass
                return

        self.x = x
        self.y = y

        for enemy in world.enemies:
            if distance([enemy.x, enemy.y], [self.x, self.y]) < enemy.radius + self.radius:
                self.hit(enemy, world)
                break

    def hit(self, enemy, world):
        enemy.get_damage(self.damage, world)
        world.bullets.remove(self)

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.calc_coords([self.x, self.y]), self.radius)