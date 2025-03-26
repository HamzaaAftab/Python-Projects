def main():
    
    dividend:int = int(input("Enter an integer to be Dividend:  "))
    divisor:int = int(input("Enter an integer to be Divisor:"))
    
    quotient: int = dividend // divisor
    remainder: int = dividend & divisor 
    
    print(f" Dividend: {dividend} \n Divisor: {divisor} \n Quotient: {quotient} \n Remainder: {remainder}")
    
if __name__ == '__main__':
    main()