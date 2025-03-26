import random

def play():
    user = input("What's your choice? r for Rock, p for Paper, s for Scissors: ")
    computer = random.choice(['r', 'p', 's']) # It allows choice between these three
    
    if user == computer:
        return 'Its a tie'
    
    if is_win(user, computer):
        return 'You Win'
    
    return "You Lost"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False
    
print(play()) # Call the function to play the game. This will run the game until the user decides to stop.
    
    