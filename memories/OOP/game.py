import pygame
import time
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1530
HEIGHT = 800


def distance(point1, point2):
    return ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5

def get_vector_length(vector: list):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5


class Sprite:
    def update(self, keys, enemies, hero):
        pass

    def draw(self, screen, camera):
        pass


class Hero(Sprite):
    def __init__(self, name, speed, x, y, color=BLUE, radius=15):
        self.name = name
        self.speed = speed
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

    def update(self, keys, enemies, hero):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def shoot(self, x, y, bullets):
        vector = [x - hero.x, y - hero.y]
        bullet = Bullet.spawn(self.x, self.y, vector, 10)
        bullets.append(bullet)

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.calc_coords([self.x, self.y]), self.radius)


class Enemy(Sprite):
    def __init__(self, x, y, speed, vision_range=200, radius=20, color=RED):
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius
        self.color = color
        self.vision_range = vision_range

        self.patrol_vector = None
        self.patrol_vector_time = None

    def update(self, keys, enemies, hero):
        if distance([self.x, self.y], [hero.x, hero.y]) < self.vision_range:
            vector = [hero.x - self.x, hero.y - self.y]
            vector_length = get_vector_length(vector)

            mini_vector = [vector[0] * self.speed / vector_length, vector[1] * self.speed / vector_length]

            self.x += mini_vector[0]
            self.y += mini_vector[1]
        else:
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

    @classmethod
    def spawn_random(cls):
        return cls(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(1, 3),
                   vision_range=random.randint(150, 250),
                   radius=random.randint(15, 25),
                   color=(random.randint(200, 255), random.randint(0, 100), random.randint(0, 100)))

    def die(self, enemies):
        enemies.remove(self)


class Bullet(Sprite):
    def __init__(self, x, y, speed, vector, color=BLACK, radius=3):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.radius = radius
        self.vector = vector

    @classmethod
    def spawn(cls, x, y, start_vector, speed):
        length = get_vector_length(start_vector)
        return cls(x, y, speed, [start_vector[0] * speed / length, start_vector[1] * speed / length])

    def update(self, keys, enemies, hero):
        self.x += self.vector[0]
        self.y += self.vector[1]

        for enemy in enemies:
            if distance([enemy.x, enemy.y], [self.x, self.y]) < enemy.radius + self.radius:
                enemy.die(enemies)
                bullets.remove(self)
                break

    def draw(self, screen, camera):
        pygame.draw.circle(screen, self.color, camera.calc_coords([self.x, self.y]), self.radius)


class Rock(Sprite):
    def __init__(self, x, y, radius=7):
        self.x = x
        self.y = y
        self.radius = radius

    def update(self, keys, enemies, hero):
        pass

    def draw(self, screen, camera):
        pygame.draw.circle(screen, BLACK, camera.calc_coords([self.x, self.y]), self.radius)

    @classmethod
    def generate_random(cls):
        return cls(random.randint(-4000, 4000), random.randint(-4000, 4000), radius=random.randint(5, 10))

    @classmethod
    def generate_many_rocks(cls, n=300):
        return [cls.generate_random() for _ in range(n)]


class Camera:
    def __init__(self, hero, width=WIDTH, height=HEIGHT):
        self.hero = hero
        self.width = width
        self.height = height
        self.mouse_coords = [0, 0]
        self.k = 0.3

    def get_center_coords(self):
        hero_coords = [self.hero.x, self.hero.y]
        vector = [self.mouse_coords[0] - hero_coords[0], self.mouse_coords[1] - hero_coords[1]]
        small_vector = [vector[0] * self.k, vector[1] * self.k]
        return [hero_coords[0] + small_vector[0], hero_coords[1] + small_vector[1]]

    def get_left_up_coords(self):
        center = self.get_center_coords()
        return [center[0] - self.width // 2, center[1] - self.height // 2]

    def calc_coords(self, global_coords):
        coords = self.get_left_up_coords()
        return [global_coords[0] - coords[0], global_coords[1] - coords[1]]

    def local_to_global(self, local_coords):
        coords = self.get_left_up_coords()
        return [coords[0] + local_coords[0], coords[1] + local_coords[1]]

    def set_mouse_coords(self, coords):
        self.mouse_coords = coords


screen = pygame.display.set_mode((WIDTH, HEIGHT))
hero = Hero('Bob', 5, 400, 400)
camera = Camera(hero=hero)
enemies = [Enemy.spawn_random() for _ in range(5)]
rocks = Rock.generate_many_rocks()
bullets = []

clock = pygame.time.Clock()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = camera.local_to_global(event.pos)
            hero.shoot(x, y, bullets)

    camera.set_mouse_coords(camera.local_to_global(pygame.mouse.get_pos()))

    keys = pygame.key.get_pressed()

    for obj in enemies + bullets + rocks + [hero]:
        obj.update(keys, enemies, hero)

    screen.fill(WHITE)

    for obj in rocks + enemies + bullets + [hero]:
        obj.draw(screen, camera)

    pygame.display.flip()

    clock.tick(60)
