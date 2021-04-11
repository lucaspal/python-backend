from upgrades.base.ship_upgrade import ShipUpgrade


class TeleportingModule(ShipUpgrade):
    def __init__(self):
        super(TeleportingModule, self).__init__("Teleporting Module")

    def get_dodge_chance(self):
        return 20
