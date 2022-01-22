import time
from classes.bullet import Bullet
import random


class Weapon:
    def __init__(self, hero, name, recharge_time=0.1, max_bullets=100):
        self.hero = hero
        self.name = name
        self.recharge_time = recharge_time
        self.bullets = self.max_bullets = max_bullets

        self.last_shoot_time = time.time()

    def shoot(self, x, y, bullets):
        if self.bullets > 0:
            if time.time() - self.last_shoot_time >= self.recharge_time:
                vector = [x - self.hero.x, y - self.hero.y]
                bullet = Bullet.spawn(self.hero.x, self.hero.y, vector, 10, damage=4)
                bullets.append(bullet)
                self.last_shoot_time = time.time()
                self.bullets -= 1


class Drobash(Weapon):
    def __init__(self, hero):
        super().__init__(hero, 'drobash', 1, max_bullets=200)

    def shoot(self, x, y, bullets):
        if self.bullets > 0:
            if time.time() - self.last_shoot_time >= self.recharge_time:
                vector = [x - self.hero.x, y - self.hero.y]
                for _ in range(5):
                    random_vector = [vector[0] + random.randint(-1000, 1000) / 10, vector[1] + random.randint(-1000, 1000) / 10]
                    bullet = Bullet.spawn(self.hero.x, self.hero.y, random_vector, 10, damage=4)
                    bullets.append(bullet)

                self.last_shoot_time = time.time()
                self.bullets -= 5
