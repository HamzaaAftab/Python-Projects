def main():
    
    num:int = int(input("Enter Till the Number you want Even Numbers: "))
    
    for i in range(0,num,2):
        num = i
        print(f"Even numbers till {num} are: {i}")
        

if __name__ == '__main__':
    main()