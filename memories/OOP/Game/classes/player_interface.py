import pygame
import colors


class PlayerInterface:
    def __init__(self, world):
        self.world = world
        self.hero = world.hero
        self.screen = world.screen
        self.main_font = pygame.font.Font('C:\\Windows\\Fonts\\ARIALN.TTF', 18)

    def draw(self):
        pygame.draw.rect(self.screen, colors.WHITE, (0, 0, 200, 50))
        pygame.draw.rect(self.screen, colors.BLACK, (0, 0, 200, 50), width=1)
        pygame.draw.circle(self.screen, colors.GOLD, (10, 12), 8)
        pygame.draw.circle(self.screen, colors.BLACK, (10, 12), 8, width=1)
        self.screen.blit(self.main_font.render(f'Монеты: {self.hero.gold}', True, colors.BLACK), (20, 2))
        self.screen.blit(self.main_font.render(f"Патроны: {self.hero.weapon.bullets}/{self.hero.weapon.max_bullets}", True, colors.BLACK), (20, 25))
