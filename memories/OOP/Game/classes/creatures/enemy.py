from classes.creatures.creature import Creature
from colors import *
import time
import random
from tools.math_ops import *
from settings import *
from classes.loot.loot import Loot
from classes.loot.loot_types import *


class Enemy(Creature):
    last_spawn_time = time.time()
    respawn_seconds = 4

    def __init__(self, x, y, speed, hp=20, vision_range=200, radius=20, color=RED):
        super().__init__(x, y, speed, hp, radius)
        self.color = color
        self.vision_range = vision_range
        self.time_after_hit = 0.5

        self.patrol_vector = None
        self.patrol_vector_time = time.time()
        self.last_hit_time = time.time()

    def update(self, keys, world):
        if time.time() - self.last_hit_time < self.time_after_hit:
            return

        hero = world.hero
        if distance([self.x, self.y], [hero.x, hero.y]) < self.vision_range:
            if distance([self.x, self.y], [hero.x, hero.y]) < self.radius + hero.radius:
                hero.get_damage(10, world)
                self.last_hit_time = time.time()

            vector = [hero.x - self.x, hero.y - self.y]
            vector_length = get_vector_length(vector)

            mini_vector = [vector[0] * self.speed / vector_length, vector[1] * self.speed / vector_length]

            self.x += mini_vector[0]
            self.y += mini_vector[1]
        else:
            self.patrol()

    def patrol(self):
        if self.patrol_vector is None or time.time() - self.patrol_vector_time > 3:
            self.generate_patrol_vector()

        self.x += self.patrol_vector[0]
        self.y += self.patrol_vector[1]

    def generate_patrol_vector(self):
        small_vector = [random.randint(-10, 10) / 10, random.randint(-10, 10) / 10]
        d = (small_vector[0] ** 2 + small_vector[1] ** 2) ** 0.5
        k = self.speed / d if d != 0 else 0
        self.patrol_vector = [small_vector[0] * k * 0.5, small_vector[1] * k * 0.5]
        self.patrol_vector_time = time.time()

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.calc_coords([self.x, self.y]), self.radius)
        pygame.draw.circle(screen, self.color, camera.calc_coords([self.x, self.y]), self.vision_range, width=1)
        self.draw_hp_bar(screen, camera)

    @classmethod
    def spawn_random(cls, world):
        while True:
            x, y = random.randint(0, WORLD_WIDTH), random.randint(0, WORLD_HEIGHT)
            ok = True
            for store in world.stores:
                if distance((x, y), (store.x, store.y)) < store.safe_radius:
                    ok = False
                    break
            if ok:
                break

        return cls(x, y, random.randint(1, 3),
                   vision_range=random.randint(150, 250),
                   radius=random.randint(15, 25),
                   color=(random.randint(200, 255), random.randint(0, 100), random.randint(0, 100)))

    def get_damage(self, damage, world):
        self.hp -= damage
        if self.hp <= 0:
            self.die(world)

    def die(self, world):
        world.loot.append(Loot.spawn_in_random_dir(self.x, self.y, GOLD, random.randint(5, 10)))
        world.enemies.remove(self)

    @classmethod
    def check_spawn(cls, world):
        enemies = world.enemies
        if len(enemies) < 20:
            if time.time() - cls.last_spawn_time > cls.respawn_seconds:
                enemies.append(cls.spawn_random(world))
                cls.last_spawn_time = time.time()
