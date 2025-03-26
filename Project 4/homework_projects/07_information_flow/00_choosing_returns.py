
MAX_AGE = 18
def is_adult(age:int):
    if age >= MAX_AGE:
        return True
    return False

# Test the function
def main():
    age = int(input("How old is this Person? "))
    print(is_adult(age))
    
if __name__ == "__main__":
    main()
        
    