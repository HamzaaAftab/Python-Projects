def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num): # It will loop till the number for example 12-> then till 12
        curr_divisor = i + 1 # Make sure to start from instead of 0
        if num % curr_divisor == 0: # For suppose i = 1, if 12 is divided by 1 then it is divisible
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()