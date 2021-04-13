import random
from enum import Enum, unique


@unique
class Weather(Enum):
    SUNNY = 1
    CLOUDY = 2
    RAINY = 3

    def __str__(self):
        return self.name

    @staticmethod
    def pick_random():
        return random.choice(list(Weather))
