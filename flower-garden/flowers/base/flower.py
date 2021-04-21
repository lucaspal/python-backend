import random
import string
from abc import ABC, abstractmethod

from weather import Weather


class Flower(ABC):
    def __init__(self, *,
                 name: string,
                 description: string,
                 height: float,
                 hydration: float,
                 max_height: float):
        self._name = name
        self._description = description
        self._height = height
        self._hydration = hydration
        self.max_height = max_height

    def __str__(self):
        if self.is_dead():
            return 'Flower Name: {name} ({description}). ' \
                   'This flower is dead.'.format(name=self._name,
                                                 description=self._description)
        else:
            return 'Flower Name: {name} ({description}). ' \
                   'It is {height} cm tall, with an hydration of {hydration}%'.format(
                        name=self._name,
                        description=self._description,
                        height=self._height,
                        hydration=self._hydration)

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def height(self):
        """ Represents the height of the flower (in centimeters). """
        return self._height

    @height.setter
    def height(self, value: float):
        if value < 0:
            self._height = 0
        else:
            self._height = value if value < self.max_height else self.max_height

    @property
    def hydration(self):
        """ Represents the hydration of the flower (in percentage). """
        return self._hydration

    @hydration.setter
    def hydration(self, value: float):
        if value < 0:
            self._hydration = 0
        if value > 100:
            self._hydration = 100
        else:
            self._hydration = value

    def process_day_with_condition(self, *, weather: Weather):
        if weather is Weather.SUNNY:
            self._on_sunny_day()
        elif weather is Weather.CLOUDY:
            self._on_cloudy_day()
        elif weather is Weather.RAINY:
            self._on_rainy_day()

    @abstractmethod
    def is_dead(self):
        raise NotImplementedError

    @abstractmethod
    def _on_rainy_day(self):
        raise NotImplementedError

    @abstractmethod
    def _on_sunny_day(self):
        raise NotImplementedError

    @abstractmethod
    def _on_cloudy_day(self):
        raise NotImplementedError

    @staticmethod
    def _draw_initial_height(min_value, max_value, *, upper_limit):
        if min_value < 0:
            raise ValueError('Min value cannot be negative')
        if max_value > upper_limit:
            raise ValueError('Max value cannot be greater than upper limit.')
        return round(min_value + (max_value - min_value) * random.random(), 1)

    @staticmethod
    def _draw_initial_hydration(min_value, max_value):
        if min_value < 0:
            raise ValueError('Min value cannot be negative.')
        if max_value > 100:
            raise ValueError('Max value cannot be greater than 100.')
        return round(min_value + (max_value - min_value) * random.random(), 1)
