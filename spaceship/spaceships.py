import math
import string
from abc import ABC
import random
from typing import List, Iterator, Callable


class Modifier:
    _flat: int
    _percentage: float

    def __init__(self, flat, percentage):
        self._flat = flat
        self._percentage = percentage

    def get_flat(self):
        return self._flat

    def get_percentage(self):
        return self._percentage

    @staticmethod
    def flat(value: int):
        return Modifier(value, 0)

    @staticmethod
    def percent(value: float):
        return Modifier(0, value)

    @staticmethod
    def calculate(base: int, modifiers: 'Iterator[Modifier]'):
        flat = sum(map(lambda x: x.get_flat(), modifiers))
        percent = sum(map(lambda x: x.getpercentage(), modifiers))
        return base + flat + math.trunc(base * percent)


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

    def get_dodge_chance(self):
        return 0

    def get_reflect_chance(self):
        return 0


# Now we define all the upgrades here
class TitaniumArmor(ShipUpgrade):
    def __init__(self):
        super(TitaniumArmor, self).__init__("Titanium Armor")

    def get_armor_modifier(self):
        return Modifier.flat(3)

    def get_hp_modifier(self):
        return Modifier.flat(250)


class AbsorptionShield(ShipUpgrade):
    def __init__(self):
        super(AbsorptionShield, self).__init__("Absorption Shield")

    def get_armor_modifier(self):
        return Modifier.percent(0.5)


class ProtonTorpedoes(ShipUpgrade):
    def __init__(self):
        super(ProtonTorpedoes, self).__init__("Proton Torpedoes")

    def get_damage_modifier(self):
        return Modifier.flat(25)


class FlareEngine(ShipUpgrade):
    def __init__(self):
        super(FlareEngine, self).__init__("Flare Engine")

    def get_armor_modifier(self):
        return Modifier.flat(3)

    def get_hp_modifier(self):
        return Modifier.percent(0.2)

    def get_damage_modifier(self):
        return Modifier.percent(0.5)


class EmpCannon(ShipUpgrade):
    def __init__(self):
        super(EmpCannon, self).__init__("EMP Cannon")

    def can_pierce_armor(self):
        return True


class TeleportingModule(ShipUpgrade):
    def __init__(self):
        super(TeleportingModule, self).__init__("Teleporting Module")

    def get_dodge_chance(self):
        return 20


class MolecularMirror(ShipUpgrade):
    def __init__(self):
        super(MolecularMirror, self).__init__("Molecular Mirror")

    def get_reflect_chance(self):
        return 10


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

    # private methods
    def _calculate_with_modifiers(
            self, value: int, func: Callable[[ShipUpgrade], Modifier]) -> int:
        modifiers = map(func, self._upgrades)
        result = Modifier.calculate(value, modifiers)
        return result


class Game:
    _attacker: Spaceship
    _defender: Spaceship

    def __init__(self, player1: Spaceship, player2: Spaceship):
        # randomize who starts
        player1_starts = (random.randint(0, 1) == 0)
        self._attacker = player1 if player1_starts else player2
        self._defender = player2 if player1_starts else player1

    def is_stalemate(self):
        return not (self._attacker.can_attack() or self._defender.can_attack())

    def game_over(self):
        return self._attacker.is_destroyed() or self._defender.is_destroyed()

    def execute_turn(self):
        # first check for dodge
        if self._defender.dodge():
            print(f"{self._defender.get_name()} dodges the attack!")

        else:
            # first check for attack reflection
            target = self._defender
            if self._defender.reflect():
                target = self._attacker
                print(f"{self._defender.get_name()} reflects attack!")

            # calculate armor including piercing
            target_armor = target.get_armor()
            if self._attacker.is_piercing():
                target_armor = math.floor(target_armor / 2)

            damage = max(1, self._attacker.get_damage() - target_armor)
            target.take_damage(damage)
            print(f"{self._attacker.get_name()} deals {damage} damage to {target.get_name()}")

        # then swap roles
        self._swap_ships()

    def _swap_ships(self):
        temp = self._defender
        self._defender = self._attacker
        self._attacker = temp


def main():
    first = Spaceship(
        "Corsair", 3, 20, 465,
        [TitaniumArmor(), FlareEngine(), EmpCannon(), MolecularMirror()])
    second = Spaceship(
        "Phoenix", 2, 15, 480,
        [AbsorptionShield(), ProtonTorpedoes(), TeleportingModule()])

    print(f"{first.get_name()} ({first.get_remaining_hp()}/{first.get_max_hp()})")
    print(f"{second.get_name()} ({second.get_remaining_hp()}/{second.get_max_hp()})")

    game = Game(first, second)
    if game.is_stalemate():
        print("Neither of the ships can attack! This is a stalemate!")
    else:
        print("Beginning battle!")

        turn = 1
        while not game.game_over():
            print(f"\n====== Turn {turn}:  ======")
            game.execute_turn()
            print(f"{first.get_name()} ({first.get_remaining_hp()}/{first.get_max_hp()})")
            print(f"{second.get_name()} ({second.get_remaining_hp()}/{second.get_max_hp()})")
            turn += 1

        winner = first if second.is_destroyed() else second
        loser = second if winner == first else first
        print(f"{loser.get_name()} has been destroyed! {winner.get_name()} wins!")
