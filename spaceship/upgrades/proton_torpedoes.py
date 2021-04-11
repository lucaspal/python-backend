from upgrades.base.modifier import Modifier
from upgrades.base.ship_upgrade import ShipUpgrade


class ProtonTorpedoes(ShipUpgrade):
    def __init__(self):
        super(ProtonTorpedoes, self).__init__("Proton Torpedoes")

    def get_damage_modifier(self):
        return Modifier.flat(25)
