AFFIRMATION: str = "I am capable of doing anything I put my mind to."
name: str = input("Enter your Name: ")

def main():
    
    
    print(f"Hello {name}, Today's Affirmation is {AFFIRMATION}")
    
    print(f"I would like you to type today's Affirmation to further Proceed {name}")
    user_feedback = input()
    
    while user_feedback != AFFIRMATION:
        print("You are not on the right path. It was not the Affirmation, Please type it correctly")
        
        # Asking the User Again
        user_feedback = input()
    
    # Outside of the Loop, If the User types the Correct Affirmation
    print(f"That's Right {name}...Good Luck for your day with your motivation")    
    
if __name__ == '__main__':
    main()