import pyjokes

def get_joke():
    jk: str = str(input("If you want to hear a Joke type Joke to proceed..!  "))
    
    if jk.lower() == "joke":
        print(pyjokes.get_joke())
    else:
        print("Invalid input. Please try again.")
        get_joke()

get_joke()