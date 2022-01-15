from classes.creature import Creature
from colors import *
from tools.math_ops import *
from settings import pygame
from classes.bullet import Bullet


class Hero(Creature):
    def __init__(self, name, speed, x, y, hp=50, color=BLUE, radius=15):
        super().__init__(x, y, speed, hp, radius)
        self.name = name
        self.color = color

    def update(self, keys, world):
        x, y = self.x, self.y
        if keys[pygame.K_w]:
            y -= self.speed
        if keys[pygame.K_a]:
            x -= self.speed
        if keys[pygame.K_s]:
            y += self.speed
        if keys[pygame.K_d]:
            x += self.speed

        can_move = True
        for rock in world.rocks:
            if distance([x, y], [rock.x, rock.y]) < rock.radius + self.radius:
                can_move = False
                break

        if can_move:
            self.x = x
            self.y = y

    def shoot(self, x, y, bullets):
        vector = [x - self.x, y - self.y]
        bullet = Bullet.spawn(self.x, self.y, vector, 10, damage=4)
        bullets.append(bullet)

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.calc_coords([self.x, self.y]), self.radius)
        self.draw_hp_bar(screen, camera)

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        print('You loose')
        exit()
