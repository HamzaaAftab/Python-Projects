def main():
    
    length1 = float(input("What is the Length of Side 1: "))
    length2 = float(input("What is the Length of Side 2: "))
    length3 = float(input("What is the Length of Side 3: "))
    
    perimeter : float = length1 + length2 + length3    
    print(f"The Perimeter of the Triangle is {perimeter}")
    
if __name__ == '__main__':
    main()