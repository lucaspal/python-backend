from core.spaceship import Spaceship


class Corsair(Spaceship):
    def __init__(self):
        super().__init__('Corsair', hp=75, damage=25, armor=8)

    def attack(self, target: Spaceship):
        target.process_damage(self.damage)
        print('attacked')
        # do something here


if __name__ == '__main__':
    corsair = Corsair()
    print(corsair.name)
