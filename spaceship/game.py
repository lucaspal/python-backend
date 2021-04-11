import math
import random

from spaceship import Spaceship


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
