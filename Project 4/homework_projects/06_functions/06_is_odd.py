def even_odd(x):
    for i in range(x):
        if i % 2 == 0:
            print(f"{i} is even", end="  ")
        else:
            print(f"{i} is odd", end="  ")

def main():
    num = int(input("Enter a Number you want to know how many times even and odd are there: "))
    eo = even_odd(num)
    print(eo, end="  ")

if __name__ == "__main__":
    main()