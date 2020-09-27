from core.spaceship import Spaceship


class BattleCruiser(Spaceship):
    def __init__(self):
        super().__init__('BattleCruiser', hp=130, damage=30, armor=15)
