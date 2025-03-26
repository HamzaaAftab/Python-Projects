import random

# Define probability of stopping early
DONE_LIKELIHOOD = 0.3  # 30% chance to stop at each step

def chaotic_counting():
    for i in range(10): # Loop till 10
        curr_num = i + 1 # Start at 1
        if done(): # If done funcion returns true then it stops
            print(f"Stopping early at {curr_num}!")
            return  # Ends function execution early
        print(curr_num) 

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD  # Simplified return

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done!")

if __name__ == "__main__":
    main()
