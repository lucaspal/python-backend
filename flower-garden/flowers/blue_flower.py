from flowers.base.flower import Flower


class BlueFlower(Flower):
    max_height = 12

    def __init__(self):
        initial_height = self._draw_initial_height(6, 7.5, upper_limit=BlueFlower.max_height)
        initial_hydration = self._draw_initial_hydration(40, 70)

        super().__init__(name='Blue Flower',
                         description='Arctic Flower',
                         height=initial_height,
                         hydration=initial_hydration,
                         max_height=BlueFlower.max_height)

    def is_dead(self):
        return self.height < 1 or self.hydration < 15

    def _on_rainy_day(self):
        self.hydration += 10
        self.height += 0.5

    def _on_sunny_day(self):
        self.hydration -= 5
        self.height -= 1

    def _on_cloudy_day(self):
        if self.hydration > 35:
            self.height += 0.5

    def _compute_height_on_new_day(self):
        if 10 < self.hydration < 40:
            self.height += 1.5
        else:
            self.height -= 1
