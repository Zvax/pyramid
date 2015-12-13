from roller import Roller

print("welcome to the random dice.py emulator\n")

roller = Roller()

while True:
    char = input("r: roll, q: quit, m: change the range\n")
    roller.dispatch(char)
