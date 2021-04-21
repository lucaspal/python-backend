from experiment import Experiment
from flowers.blue_flower import BlueFlower
from flowers.red_flower import RedFlower
from flowers.yellow_flower import YellowFlower


def main():
    flowers = [YellowFlower(), RedFlower(), BlueFlower()]
    number_of_days = 1000

    experiment = Experiment(days=number_of_days, flowers=flowers)
    experiment.run()


if __name__ == '__main__':
    main()
