def main():
    
    # Input Temperature in Fahrenheit
    fahrenheit = float(input("Enter Temperature in Fahrenheit: "))
    
    # Converting it to Celsius by using this equation
    celsius = (fahrenheit - 32) * 5.0/9.0
    
    # Printing the converted temperature in Celsius
    print(f"Given Temperature in Celsius is: {celsius}C")
    
if __name__ == '__main__':
    main()