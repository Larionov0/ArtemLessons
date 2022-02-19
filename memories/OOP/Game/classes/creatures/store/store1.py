from classes.weapons.weapon import Weapon
from tools.math_ops import normalize_victor
import time
from classes.creatures.bullet import Bullet


class TihiyPistolet(Weapon):
    def __init__(self, hero, name='Тихий пистолет', damage=6, recharge_time=0.5, max_bullets=150):
        super().__init__(hero, name, damage, recharge_time, max_bullets, description='Очень тихий но слабый пистолет')


class AutomatBobby(Weapon):
    def __init__(self, hero, name='Автомат Бобби', damage=4, recharge_time=0.1, max_bullets=300):
        super().__init__(hero, name, damage, recharge_time, max_bullets)


class Dvoostvolka(Weapon):
    def __init__(self, hero, name='Двустволка', damage=5, distance=5, recharge_time=1, max_bullets=70):
        super().__init__(hero, name, damage, recharge_time, max_bullets)

    def shoot(self, x, y, bullets):
        if self.bullets > 0:
            if time.time() - self.last_shoot_time >= self.recharge_time:
                vector = [x - self.hero.x, y - self.hero.y]
                perp1 = normalize_victor([-vector[1], vector[0]], 5)
                perp2 = normalize_victor([vector[1], -vector[0]], 5)

                bullets.append(Bullet.spawn(self.hero.x + perp1[0], self.hero.y + perp1[1], vector, 7, damage=self.damage))
                bullets.append(Bullet.spawn(self.hero.x + perp2[0], self.hero.y + perp2[1], vector, 7, damage=self.damage))
                self.last_shoot_time = time.time()
                self.bullets -= 2


store = {
    'weapons': [
        {
            'weapon': TihiyPistolet(None),
            'price': 120
        },
        {
            'weapon': AutomatBobby(None),
            'price': 250
        },
        {
            'weapon': Dvoostvolka(None),
            'price': 200
        }
    ]
}
