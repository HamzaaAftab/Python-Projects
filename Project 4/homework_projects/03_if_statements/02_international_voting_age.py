PAKISTAN_AGE = 18
ENGLAND_AGE = 21
AUSTRALIAN_AGE = 24

def main():
    
    # Ask the user to enter their age
    user_age = int(input("Enter your age: "))
    
    if user_age >= PAKISTAN_AGE:
        print(f"You are eligible to vote in Pakistan where age eligibility is {PAKISTAN_AGE}.".format())
    else:
        print(f"You are not eligible to vote in Pakistan. Your age is less than {PAKISTAN_AGE}.")
        
    if user_age >= ENGLAND_AGE:
        print(f"You are eligible to vote in England where age eligibility is {ENGLAND_AGE}.".format())
    else:
        print(f"You are not eligible to vote in England. Your age is less than {ENGLAND_AGE}.")
        
    if user_age >= AUSTRALIAN_AGE:
        print(f"You are eligible to vote in Australia where age eligibility is {AUSTRALIAN_AGE}.".format())
    else:
        print(f"You are not eligible to vote in Australia. Your age is less than {AUSTRALIAN_AGE}.")
    
    
if __name__ == '__main__':
    main()