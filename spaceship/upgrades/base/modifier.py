import math
from typing import Iterator


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
