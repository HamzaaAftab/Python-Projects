
def double(num: int):
    return num * 2

def square(num:int):
    return num ** 2

def cube(num: int):
    return num ** 3

def main():
    num: int = int(input("Enter a Number: "))
    do = double(num)
    sq = square(num)
    cb = cube(num)
    print(f"{num} doubled is {do}")
    print(f"{num} squared is {sq}")
    print(f"{num} cubed is {cb}")
    
if __name__ == '__main__':
    main()