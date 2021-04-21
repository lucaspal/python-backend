import random
from typing import List

from experiment import Experiment
from flowers.base.flower import Flower
from flowers.blue_flower import BlueFlower
from flowers.red_flower import RedFlower
from flowers.yellow_flower import YellowFlower


def main():
    number_of_flowers = 10
    number_of_days = 1000

    flowers = _pick_flowers(number_of_flowers)

    experiment = Experiment(days=number_of_days, flowers=flowers)
    experiment.run()


def _pick_flowers(number: int) -> List[Flower]:
    flower_types = [YellowFlower, RedFlower, BlueFlower]
    return [random.choice(flower_types)() for _ in range(number)]


if __name__ == '__main__':
    main()
