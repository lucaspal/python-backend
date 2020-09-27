from core.opponents import Opponents
from core.spaceship import Spaceship


def parse_details(details_string: str):
    details_string.replace(' ', '')
    parsed_details = details_string.split(',')

    if len(parsed_details) != 3:
        raise ValueError('')

    return list(map(int, parsed_details))


def init():
    battleship_one = battleship_from_cli(1)
    battleship_two = battleship_from_cli(2)
    return Opponents([battleship_one, battleship_two])


def battleship_from_cli(battleship_number: int):
    battleship_name = input(f'Enter battleship {battleship_number} name: ')
    battleship_details = input('Enter battleship 1 details (HP, Armor, Damage) separated by commas:')
    parsed_details = parse_details(battleship_details)

    return Spaceship(name=battleship_name, hp=parsed_details[0], armor=parsed_details[1],
                     damage=parsed_details[2])


if __name__ == '__main__':
    opponents = init()
    print('\n')
    round_number = 1

    # cover edge cases (e.g. battle can't begin)
    while opponents.should_continue():
        print(f'Round {round_number} - {opponents.attacker.name} is attacking, {opponents.defender.name} is defending.')
        opponents.next_round()
        round_number += 1

        print('=== Stats after round ===')
        print(f'Attacker stats: {opponents.attacker.to_string()}')
        print(f'Defender stats: {opponents.defender.to_string()}')
        print('==========================\n')

    print('Thanks for having played Battleships.')
