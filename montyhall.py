import random
import numpy as np


numSamples = 100000
numDoors = 3 # might not need this if just doing 3 doors, can just hard code it this way
doors = [0, 1, 2]
numCorrectFlip = 0
numCorrectNoFlip = 0

for _ in range(numSamples):
    correctDoor = random.randint(0, 2)
    guess = random.randint(0, 2)
    if (guess == correctDoor):
        pre_choices = doors.copy().remove(correctDoor)
        removeDoor = random.randint(0, 1)
        choices = doors.copy() - (pre_choices - pre_choices[removeDoor]) # the concept here is right, but incorrect python usage.
    else:
        choices = doors.copy() - (doors - correctDoor - guess)
    flip = random.randint(0, 1)
    if flip:
        guess = 1 - doors.index(guess)
        if (guess == correctDoor):
            numCorrectFlip += 1
    else:
        if (guess == correctDoor):
            numCorrectNoFlip += 1

print("amount correct from flip guess: ", numCorrectFlip / numSamples)
print("amount correct from no flip guess: ", numCorrectNoFlip / numSamples)
    




