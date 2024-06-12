import random

number_to_guess = random.randint(1, 100)
user_guess = None

print("Guess the number between 1 and 100")

while user_guess != number_to_guess:
    user_guess = int(input("Enter your guess: "))
    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You guessed the right number.")

