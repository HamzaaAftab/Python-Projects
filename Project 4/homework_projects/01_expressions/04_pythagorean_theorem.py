import math

def main():
    try:
        # Enter the Length for AB
        ab: float = float(input("Enter the Length for AB: "))
        ac: float = float(input("Enter the Length for AC: "))

        # Calculating the Hypotenuse
        hypotenuse: float = math.sqrt(ab**2 + ac**2)

        # Printing the Result
        print("Hypotenuse is: ", str(hypotenuse))

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == '__main__':
    main()
