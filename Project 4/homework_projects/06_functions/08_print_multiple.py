def print_multiple(message, repeats):
    for _ in range(repeats):  # Loop repeats times
        print(message)  # Print the message

def main():
    message = input("Please type a message: ")  # Get the message from user
    repeats = int(input("Enter a number of times to repeat your message: "))  # Get the repeat count
    print_multiple(message, repeats)  # Call function

# Run the program
if __name__ == "__main__":
    main()
