
MINIMUM_HEIGHT:int = 50

def main():
    
    # Prompt the user to enter their height in centimeters
    user_height = int(input("Enter your height: "))
    
    if user_height >= MINIMUM_HEIGHT:
        print("You are tall enough to ride.")
    else:
        print("You are not tall enough to ride.")
    
    
if __name__ == '__main__':
    main()