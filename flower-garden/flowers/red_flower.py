from flowers.base.flower import Flower


class RedFlower(Flower):
    max_height = 10

    def __init__(self):
        initial_height = self._draw_initial_height(4, 6, upper_limit=RedFlower.max_height)
        initial_hydration = self._draw_initial_hydration(30, 60)

        super().__init__(name='Red Flower',
                         description='Temperate Flower',
                         height=initial_height,
                         hydration=initial_hydration,
                         max_height=RedFlower.max_height)

    def is_dead(self):
        return self.height < 2.5

    def _on_rainy_day(self):
        self.hydration += 10
        self._shared_height_computation()

    def _on_sunny_day(self):
        self.hydration -= 5
        if 20 <= self.hydration <= 85:
            self.height += 1
        else:
            self._shared_height_computation()

    def _on_cloudy_day(self):
        self.hydration -= 2
        self._shared_height_computation()

    def _shared_height_computation(self):
        if self.hydration < 20 or self.hydration > 85:
            self.height -= 0.5
