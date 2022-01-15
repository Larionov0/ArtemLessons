import pygame
import time
import random
from colors import *
from classes.hero import Hero
from classes.enemy import Enemy
from classes.rabbit import Rabbit
from classes.camera import Camera
from classes.rock import Rock
from settings import WIDTH, HEIGHT

pygame.init()


class World:
    def __init__(self):
        self.hero = Hero('Bob', 5, 400, 400)
        self.camera = Camera(hero=self.hero, width=WIDTH, height=HEIGHT)
        self.enemies = [Enemy.spawn_random() for _ in range(5)]
        self.enemies.append(Rabbit(300, 300, 4, 10))
        self.rocks = Rock.generate_many_rocks()
        self.bullets = []
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = self.camera.local_to_global(event.pos)
                    self.hero.shoot(x, y, self.bullets)

            self.camera.set_mouse_coords(self.camera.local_to_global(pygame.mouse.get_pos()))

            keys = pygame.key.get_pressed()

            for obj in self.enemies + self.bullets + self.rocks + [self.hero]:
                obj.update(keys, self)

            self.screen.fill(WHITE)

            for obj in self.rocks + self.enemies + self.bullets + [self.hero]:
                obj.draw(self.screen, self.camera)

            Enemy.check_spawn(self.enemies)

            pygame.display.flip()
            self.clock.tick(60)


World().run()
