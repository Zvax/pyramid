from dice import Dice


class Roller:
    """roller manager"""

    def __init__(self):
        self.defaultMinValue = 1
        self.defaultMaxValue = 6

    def roll(self):
        dice = Dice(self.defaultMinValue, self.defaultMaxValue)
        dice.roll()

    def dispatch(self, x):
        if x == 'r':
            self.roll()
        elif x == 'q':
            quit()
        elif x == 'm':
            self.modify()

    def modify(self):
        self.defaultMinValue = int(input("enter min value:\n"))
        self.defaultMaxValue = int(input("enter max value:\n"))
