from typing import List

from core.spaceship import Spaceship


class Opponents:
    """
    Class representing the two opponents fighting against each other.
    """

    def __init__(self, opponents: List[Spaceship]):
        if len(opponents) != 2:
            raise ValueError('Exactly 2 opponents must fight against each other.')
        self.opponents = opponents
        self.opponent_one = opponents[0]
        self.opponent_two = opponents[1]

        # Can randomize to cover the extra point
        self.attacker: Spaceship = self.opponent_one
        self.defender: Spaceship = self.opponent_two

    def should_continue(self):
        return len(list(filter(lambda player: player.is_destroyed(), self.opponents))) == 2

    def next_round(self):
        # attack step
        self.attacker.attack(self.defender)

        # could be probably be done in a smarter way
        new_attacker = self.defender
        if new_attacker.can_attack():
            self.defender = self.attacker
            self.attacker = new_attacker

    # not used at the moment
    def current_attacker(self):
        return self.opponent_one
