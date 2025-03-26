def greet(name: str):
    return name
    
    
def main():
    name: str = input("Enter your Name: ")
    print(f"Hello, {greet(name)}, Have a Nice Day..!")

if __name__ == "__main__":
    main()    