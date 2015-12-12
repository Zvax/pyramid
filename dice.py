from random import randint


class Dice:
    """a simple dice.py class"""

    def __init__(self, minvalue, maxvalue):
        self.min = minvalue
        self.max = maxvalue

    def roll(self):
        print("rolled " + str(randint(self.min, self.max)))
