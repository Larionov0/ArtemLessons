from classes.creatures.creature import BaseSprite
import pygame
import colors
from tools.math_ops import distance, get_vector_length


class Store(BaseSprite):
    def __init__(self, x, y, width=350, height=350, safe_radius=800, extrusion_speed=15, products=None):
        super().__init__(x, y)
        self.width = width
        self.height = height
        if products is None:
            self.products = {
                'weapons': [],
                'ammo': []
            }
        self.image = pygame.image.load('img/store.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.safe_radius = safe_radius
        self.extrusion_speed = extrusion_speed

    def update(self, keys, world):
        for obj in world.enemies + world.loot:
            if distance((self.x, self.y), (obj.x, obj.y)) < self.safe_radius:
                vector = (obj.x - self.x, obj.y - self.y)
                d = get_vector_length(vector)
                k = self.extrusion_speed / d if d != 0 else 0
                extrusion_vector = (vector[0] * k, vector[1] * k)
                obj.x = obj.x + extrusion_vector[0]
                obj.y = obj.y + extrusion_vector[1]

    def draw(self, screen, camera):
        # pygame.draw.rect(screen, (155, 100, 50), (self.x, self.y, self.width, self.height), border_radius=10)
        # pygame.draw.rect(screen, (155, 250, 250), (self.x + 10, self.y + 10, self.width / 10, self.height / 10))  # window
        x, y = camera.calc_coords((self.x - self.width / 2, self.y - self.height / 2))
        screen.blit(self.image, (x, y, self.width, self.height))
        pygame.draw.circle(screen, colors.BLACK, camera.calc_coords((self.x, self.y)), self.safe_radius, 1)
