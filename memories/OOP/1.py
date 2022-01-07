class Hero:
    def __init__(self, name, hp, attack, armor):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.armor = armor

    def say_hi(self):
        print(f"{self.name}: Hello")

    def __str__(self):
        return f"Герой {self.name} (hp:{self.hp}/{self.max_hp}; attack: {self.attack})"

    def __add__(self, other):  # +
        return self.hp + other.hp


h1 = Hero('Assasin', 20, 8, 0)
h2 = Hero('Warrior', 30, 4, 2)
h3 = Hero('Mage', 24, 3, 0)

print(h1 + h2)
