import random

num_samples = 10000
correct_flip_guesses = 0
correct_no_flip_guesses = 0
flip = True

for _ in range(2):
    for _ in range(num_samples):
        doors = [0, 1, 2]
        correct_door = random.randint(0, 2)
        
        # Player makes an initial guess
        initial_guess = random.randint(0, 2)
        
        # Host reveals a door that is not the correct door and not the initial guess
        remaining_doors = [door for door in doors if door != initial_guess and door != correct_door]
        revealed_door = random.choice(remaining_doors)
        
        # Determine the other door that was not guessed initially and not revealed
        other_door = [door for door in doors if door != initial_guess and door != revealed_door][0]
        
        if flip:
            final_guess = other_door
        else:
            final_guess = initial_guess
        
        # Check if the final guess is correctif final_guess == correct_door:
        if final_guess == correct_door:
            if flip:
                correct_flip_guesses += 1
            else:
                correct_no_flip_guesses += 1
    flip = False

print("percent correct with flip: ", correct_flip_guesses / num_samples * 100)
print("percent correct without flip: ", correct_no_flip_guesses / num_samples * 100)
