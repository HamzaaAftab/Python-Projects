def main():
    
    # Enter Feet
    feet: float = float(input("Enter Feet: "))
    
    # Converting it into Inches
    inches:float = feet * 12
    
    #Printing the Result
    print(f"Feet {feet} in {inches}")
    
if __name__ == '__main__':
    main()