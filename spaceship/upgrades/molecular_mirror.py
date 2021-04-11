from upgrades.base.ship_upgrade import ShipUpgrade


class MolecularMirror(ShipUpgrade):
    def __init__(self):
        super(MolecularMirror, self).__init__("Molecular Mirror")

    def get_reflect_chance(self):
        return 10
