import random
import string
from typing import List, Callable

from upgrades.base.modifier import Modifier
from upgrades.base.ship_upgrade import ShipUpgrade


# Main spaceship class
class Spaceship:
    _name: string
    _base_armor: int
    _base_damage: int
    _base_hp: int
    _upgrades: List[ShipUpgrade]
    _damage_taken: int

    def __init__(self, name: string, armor: int, damage: int,
                 hp: int, upgrades: List[ShipUpgrade]):
        self._name = name
        self._base_armor = armor
        self._base_damage = damage
        self._base_hp = hp
        self._upgrades = upgrades
        self._damage_taken = 0

    # public methods
    def get_name(self):
        return self._name

    # properties with upgrades
    def get_max_hp(self):
        return self._calculate_with_modifiers(
            self._base_hp, lambda x: x.get_hp_modifier())

    def get_armor(self):
        return self._calculate_with_modifiers(
            self._base_armor, lambda x: x.get_armor_modifier())

    def get_damage(self):
        return self._calculate_with_modifiers(
            self._base_damage, lambda x: x.get_damage_modifier())

    def is_piercing(self):
        return any(map(lambda x: x.can_pierce_armor(), self._upgrades))

    def get_dodge(self):
        return sum(map(lambda x: x.get_dodge_chance(), self._upgrades))

    def get_reflect(self):
        return sum(map(lambda x: x.get_reflect_chance(), self._upgrades))

    # ship state
    def get_remaining_hp(self) -> int:
        return max(0, self.get_max_hp() - self._damage_taken)

    def can_attack(self) -> bool:
        return self.get_damage() > 0

    def is_destroyed(self) -> bool:
        return self.get_remaining_hp() == 0

    # actions
    def dodge(self) -> bool:
        die_value = random.randint(1, 100)
        return die_value <= self.get_dodge()

    def reflect(self) -> bool:
        die_value = random.randint(1, 100)
        return die_value <= self.get_reflect()

    def take_damage(self, damage):
        self._damage_taken = self._damage_taken + damage

    # private method
    def _calculate_with_modifiers(
            self, value: int, func: Callable[[ShipUpgrade], Modifier]) -> int:
        modifiers = map(func, self._upgrades)
        result = Modifier.calculate(value, modifiers)
        return result
