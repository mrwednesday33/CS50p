import random
while True:
    level_input = input("Level: ")
    if level_input.isdigit() and int(level_input) > 0:
        level = int(level_input)
        break

number = random.randint(1, level)

while True:
    guess_input = input("Guess: ")
    if guess_input.isdigit() and int(guess_input) > 0:
        guess = int(guess_input)
        if guess < number:
            print("Too small!")
        elif guess > number:
            print("Too large!")
        else:
            print("Just right!")
            break