from upgrades.base.ship_upgrade import ShipUpgrade


class EmpCannon(ShipUpgrade):
    def __init__(self):
        super(EmpCannon, self).__init__("EMP Cannon")

    def can_pierce_armor(self):
        return True
