import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""  # Empty string for feedback

    while feedback != "c":
        if low > high:  # Check if the range is invalid
            print("Error: The range collapsed! You may have given incorrect feedback.")
            return  # Exit the function instead of breaking
        
        guess = random.randint(low, high)  # Computer makes a guess
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == "h":  
            high = guess - 1  # Adjust high limit
        elif feedback == "l":  
            low = guess + 1  # Adjust low limit
        elif feedback != "c":  
            print("Invalid input! Please enter 'H', 'L', or 'C'.")  # Handle invalid input

    print(f"🎉 Congratulations! The computer guessed your number: {guess}")

# Call the function
computer_guess(500)
