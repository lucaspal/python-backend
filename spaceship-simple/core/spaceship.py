class Spaceship:
    def __init__(self, name, hp, armor, damage):
        self.name = name
        self.hp = hp
        self.armor = armor
        self.damage = damage

    def is_destroyed(self):
        return self.hp > 0

    def can_attack(self):
        return self.damage > 0

    def process_damage(self, damage: int):
        if damage > self.hp:
            self.hp = 0
        else:
            self.hp -= damage

    def attack(self, target):
        target.process_damage(self.damage)

    def to_string(self):
        return f'name: {self.name} | hp: {self.hp} | damage {self.damage} | armor: {self.armor}'
