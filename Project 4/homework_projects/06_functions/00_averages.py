def average(a:float, b:float):
    
    sum = a + b
    return sum

def main():
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    
    average_value = average(num1, num2)
    print("Average of the two numbers:", average_value)
    
if __name__ == "__main__":
    main()