from upgrades.base.modifier import Modifier
from upgrades.base.ship_upgrade import ShipUpgrade


class AbsorptionShield(ShipUpgrade):
    def __init__(self):
        super(AbsorptionShield, self).__init__("Absorption Shield")

    def get_armor_modifier(self):
        return Modifier.percent(0.5)
