from classes.creatures.creature import BaseSprite
import pygame
import colors


class Store(BaseSprite):
    def __init__(self, x, y, width=150, height=120, products=None):
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

    def draw(self, screen, camera):
        # pygame.draw.rect(screen, (155, 100, 50), (self.x, self.y, self.width, self.height), border_radius=10)
        # pygame.draw.rect(screen, (155, 250, 250), (self.x + 10, self.y + 10, self.width / 10, self.height / 10))  # window
        x, y = camera.calc_coords((self.x, self.y))
        screen.blit(self.image, (x, y, self.width, self.height))
