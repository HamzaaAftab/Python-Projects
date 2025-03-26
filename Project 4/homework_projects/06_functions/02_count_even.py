def count_even(lst=None): 
    if lst is None:
        lst = []  # Initialize an empty list
    
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Stop when the user presses enter
            break
        try:
            lst.append(int(user_input))  # Convert input to integer and add to the list
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    even_count = sum(1 for num in lst if num % 2 == 0)  # Count even numbers
    print(f"Number of even numbers in the list: {even_count}")

# Call the function
count_even()
