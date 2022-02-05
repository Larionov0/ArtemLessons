from classes.creatures.creature import Creature
from colors import *
from tools.math_ops import *
from settings import pygame
from classes.weapons.weapon import Drobash
import classes.loot.loot_types as loot_types
import time


class Hero(Creature):
    def __init__(self, name, speed, x, y, hp=50, color=BLUE, radius=15):
        super().__init__(x, y, speed, hp, radius)
        self.name = name
        self.color = color
        self.weapon = Drobash(self)
        self.gold = 50

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

        for loot in world.loot:
            if distance([self.x, self.y], [loot.x, loot.y]) < self.radius + loot.radius:
                if loot.type == loot_types.GOLD:
                    self.gold += loot.amount
                    loot.destroy(world)

    def shoot(self, x, y, bullets):
        self.weapon.shoot(x, y, bullets)

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.calc_coords([self.x, self.y]), self.radius)
        self.draw_hp_bar(screen, camera)
        self.draw_reload_bar(screen, camera)

    def draw_reload_bar(self, screen, camera):
        proshlo = time.time() - self.weapon.last_shoot_time
        if proshlo > self.weapon.recharge_time:
            proshlo = self.weapon.recharge_time
        self.draw_bar(screen, camera, 5, self.radius*2 - 4, 8, proshlo, self.weapon.recharge_time, front_color=RED)

    def get_damage(self, damage, world):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        print('You loose')
        exit()
