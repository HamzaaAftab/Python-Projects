def print_ones_digit(num):
    ones_digit = num % 10  # Extract the ones digit using modulo operator
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))  # Get user input and convert it to an integer
    print_ones_digit(num)  # Call the function with the user-provided number

# Run the program
if __name__ == "__main__":
    main()
