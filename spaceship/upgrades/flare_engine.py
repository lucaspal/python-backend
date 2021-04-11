from upgrades.base.modifier import Modifier
from upgrades.base.ship_upgrade import ShipUpgrade


class FlareEngine(ShipUpgrade):
    def __init__(self):
        super(FlareEngine, self).__init__("Flare Engine")

    def get_armor_modifier(self):
        return Modifier.flat(3)

    def get_hp_modifier(self):
        return Modifier.percent(0.2)

    def get_damage_modifier(self):
        return Modifier.percent(0.5)
