import pygame
import time
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1000
HEIGHT = 700


class Sprite:
    def update(self, keys):
        pass

    def draw(self, screen):
        pass


class Hero(Sprite):
    def __init__(self, name, speed, x, y, color=BLUE, radius=30):
        self.name = name
        self.speed = speed
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def update(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Enemy(Sprite):
    def __init__(self, x, y, speed, radius=40, color=RED):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = color

    def update(self, keys):
        x_dir = random.randint(-1, 1)
        y_dir = random.randint(-1, 1)

        self.x += self.speed * x_dir
        self.y += self.speed * y_dir

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
heroes = [
    Hero('Bob', 7, 400, 400, (0, 0, 255), 50),
    Hero('Bob', 6, 400, 400, (0, 100, 255), 80),
    Hero('Bob', 5, 400, 400, (0, 150, 200), 100),
]
heroes.reverse()
clock = pygame.time.Clock()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    for hero in heroes:
        hero.update(keys)

    screen.fill(WHITE)

    for hero in heroes:
        hero.draw(screen)
    pygame.display.flip()

    clock.tick(60)
