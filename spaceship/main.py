from game import Game
from spaceship import Spaceship
from upgrades.absorption_shield import AbsorptionShield
from upgrades.emp_cannon import EmpCannon
from upgrades.flare_engine import FlareEngine
from upgrades.molecular_mirror import MolecularMirror
from upgrades.proton_torpedoes import ProtonTorpedoes
from upgrades.teleporting_module import TeleportingModule
from upgrades.titanium_armor import TitaniumArmor


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


if __name__ == '__main__':
    main()
