from typing import List

from flowers.base.flower import Flower
from weather import Weather


class Experiment:
    def __init__(self, days: int, flowers: List[Flower]):
        self._days = days
        self.flowers = flowers
        self._current_day = 0

    def process_day(self):
        """ Processing of a new day simulates weather conditions and see how flowers react.
        You will see the results of this printed to the console. """

        weather_condition = Weather.pick_random()
        print('=> Day {current_day}/{total_days} [Today is {weather}]'.format(current_day=self._current_day + 1,
                                                                              total_days=self._days,
                                                                              weather=weather_condition))

        list(map(lambda flower: flower.process_day_with_condition(weather=weather_condition), self.flowers))
        self._print_state()
        print("\n")
        self._current_day += 1

    def is_over(self):
        """ The experiment is over when all days have passed or if all flowers are dead. """
        return self._current_day == self._days or all(map(lambda flower: flower.is_dead(), self.flowers))

    def _print_state(self):
        """ Prints, in the console, the statistics of the day. """
        flowers_alive = len(list(filter(lambda f: not f.is_dead(), self.flowers)))
        print('\tHealthy flowers:\t{num}'.format(num=flowers_alive))
        print('\tDead flowers:\t\t{num}'.format(num=len(self.flowers) - flowers_alive))
        print('=> Flower Details')
        list(map(lambda flower: print(f'\t {flower}'.format(flower=flower)), self.flowers))
