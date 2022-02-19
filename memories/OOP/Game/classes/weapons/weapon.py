import time
from classes.creatures.bullet import Bullet
import random


class Weapon:
    def __init__(self, hero, name, damage, recharge_time=0.1, max_bullets=100, description='', img_file=None):
        self.hero = hero
        self.name = name
        self.recharge_time = recharge_time
        self.bullets = self.max_bullets = max_bullets
        self.damage = damage
        self.description = description
        self.img = img_file  # FIXME: создать изображение

        self.last_shoot_time = time.time()

    def set_hero(self, hero):
        self.hero = hero

    def shoot(self, x, y, bullets):
        if self.bullets > 0:
            if time.time() - self.last_shoot_time >= self.recharge_time:
                vector = [x - self.hero.x, y - self.hero.y]
                bullet = Bullet.spawn(self.hero.x, self.hero.y, vector, 10, damage=self.damage)
                bullets.append(bullet)
                self.last_shoot_time = time.time()
                self.bullets -= 1


class Drobash(Weapon):
    def __init__(self, hero):
        super().__init__(hero, 'drobash', 4, 1, max_bullets=200)

    def shoot(self, x, y, bullets):
        if self.bullets > 0:
            if time.time() - self.last_shoot_time >= self.recharge_time:
                vector = [x - self.hero.x, y - self.hero.y]
                for _ in range(5):
                    random_vector = [vector[0] + random.randint(-500, 500) / 10, vector[1] + random.randint(-500, 500) / 10]
                    bullet = Bullet.spawn(self.hero.x, self.hero.y, random_vector, 10, damage=self.damage)
                    bullets.append(bullet)

                self.last_shoot_time = time.time()
                self.bullets -= 5
