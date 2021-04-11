from upgrades.base.modifier import Modifier
from upgrades.base.ship_upgrade import ShipUpgrade


class TitaniumArmor(ShipUpgrade):
    def __init__(self):
        super(TitaniumArmor, self).__init__("Titanium Armor")

    def get_armor_modifier(self):
        return Modifier.flat(3)

    def get_hp_modifier(self):
        return Modifier.flat(250)
