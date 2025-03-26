import random # Import random to generate random numbers for dice


def main():
    for i in range(3): # It will rull dice 3 times 
        dice1= roll_dice() # Call Functions
        dice2= roll_dice() # Call Functions
        print(f"Role: {i+1} \n dice 1 shows: {dice1} \n dice 2 shows: {dice2}")
def roll_dice():
    return random.randint(1,6) #     
    
if __name__ == "__main__":
    main()