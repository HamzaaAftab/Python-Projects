def count_numbers():
    count_dict = {}  # Empty dictionary to store occurrences

    while True:
        num = input("Enter a number (or press Enter to stop): ")  # Take input
        
        if num == "":  # If user presses Enter, stop loop
            break
        
        num = int(num)  # Convert input to integer
        
        if num in count_dict:
            count_dict[num] += 1  # If number exists, increase count
        else:
            count_dict[num] = 1  # If new number, initialize with 1

    for number, count in count_dict.items():
        print(f"{number} appears {count} times.")  # Print occurrences

if __name__ == "__main__":
    count_numbers()
