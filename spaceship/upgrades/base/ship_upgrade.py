import string
from abc import ABC

from upgrades.base.modifier import Modifier


# Base class for all upgrades.
class ShipUpgrade(ABC):
    _name: string

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def get_armor_modifier(self):
        return Modifier(0, 0)

    def get_hp_modifier(self):
        return Modifier(0, 0)

    def get_damage_modifier(self):
        return Modifier(0, 0)

    def can_pierce_armor(self):
        return False

    @staticmethod
    def get_dodge_chance():
        return 0

    def get_reflect_chance(self):
        return 0
