# Coin flip: random.random
import random

print("Welcome to the virtual coin toss game")
input("Press Enter to start ...")
random_number = random.random()
if random_number >= 0.5:
    print("Head")
else:
    print("Tail")

# To see the chosen number:
print(random_number, "Random number")
