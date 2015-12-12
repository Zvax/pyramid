from dice import Dice


print("welcome to the random dice.py emulator\n")


def leave():
    quit()


def roll():
    dice = Dice(1,6)
    dice.roll()


def dispatch(x):
    if x == 'r':
        roll()
    elif x == 'q':
        leave()


while True:
    char = input("r: roll, q: quit\n")
    dispatch(char)






