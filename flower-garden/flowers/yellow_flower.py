from flowers.base.flower import Flower


class YellowFlower(Flower):
    max_height = 20

    def __init__(self):
        initial_height = self._draw_initial_height(6, 9, upper_limit=YellowFlower.max_height)
        initial_hydration = self._draw_initial_hydration(20, 35)

        super().__init__(name='Yellow Flower',
                         description='Arid Flower',
                         height=initial_height,
                         hydration=initial_hydration,
                         max_height=YellowFlower.max_height)

    def is_dead(self):
        return self.height < 4

    def _on_rainy_day(self):
        self.hydration += 20
        self._shared_height_computation()

    def _on_sunny_day(self):
        self.hydration -= 5
        self._shared_height_computation()

    def _on_cloudy_day(self):
        self.hydration -= 5
        self._shared_height_computation()

    def _shared_height_computation(self):
        if 10 < self.hydration < 40:
            self.height += 1.5
        else:
            self.height -= 1
