import pygame
from colors import *
from classes.creatures.hero import Hero
from classes.creatures.enemy import Enemy
from classes.creatures.rabbit import Rabbit
from classes.camera import Camera
from classes.creatures.rock import Rock
from settings import WIDTH, HEIGHT
from classes.player_interface import PlayerInterface
from classes.creatures.store.store import Store

pygame.init()


class World:
    def __init__(self):
        self.hero = Hero('Bob', 5, 150, 150)
        self.camera = Camera(hero=self.hero, width=WIDTH, height=HEIGHT)
        self.stores = [Store(100, 100)]
        self.enemies = [Enemy.spawn_random(self) for _ in range(5)]
        self.enemies.append(Rabbit(300, 300, 4, 10))
        self.rocks = Rock.generate_many_rocks()
        self.bullets = []
        self.loot = []
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.interface = PlayerInterface(self)

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = self.camera.local_to_global(event.pos)
                    self.hero.shoot(x, y, self)

            self.camera.set_mouse_coords(self.camera.local_to_global(pygame.mouse.get_pos()))

            keys = pygame.key.get_pressed()

            for obj in self.loot + self.enemies + self.bullets + self.rocks + self.stores + [self.hero]:
                obj.update(keys, self)

            self.screen.fill(WHITE)

            for obj in self.loot + self.rocks + self.enemies + self.bullets + self.stores + [self.hero]:
                obj.draw(self.screen, self.camera)

            self.interface.draw()

            Enemy.check_spawn(self)

            pygame.display.flip()
            self.clock.tick(60)


World().run()
