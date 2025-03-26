def main():

    even:int = int(input("Enter the till the Number you want even of: "))
    for i in range(0,even,2):
        num= i 
        print(f'The  first twenty Even Numbers are: {num}')


if __name__ == '__main__':
    main()