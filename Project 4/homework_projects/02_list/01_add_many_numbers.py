def main():

    # Input List
    li :list = [34,6,10,20,40]
    
    # Loop to add all input numbers
    sum = 0
    for i in li:
        sum += int(i)
        
    # Output the sum
    print("Sum of all numbers:", sum)

if __name__ == "__main__":
    main()