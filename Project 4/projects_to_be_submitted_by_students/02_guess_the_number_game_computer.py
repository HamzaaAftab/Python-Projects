import random

def guess(x):
    random_number = random.randint(1, x)  # Generate a random number between 1 and x
    guess = 0  # Initializing guess to an invalid number to ensure loop starts

    while guess != random_number:  # Continue until user guesses correctly
        guess = int(input(f"Guess a number between 1 and {x}: "))  # Take user input
        
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")

    print(f"🎉 Congratulations! You guessed the correct number: {random_number}")

# Function Call
guess(10)
