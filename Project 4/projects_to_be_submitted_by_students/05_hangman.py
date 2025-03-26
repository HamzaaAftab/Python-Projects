from words import words # importing words from words
import random

def get_valid_word(word):
    word = random.choice(words)
    
    while '-' in word or'' in word:
        word = random.choice(words)
    
    return word

def play_hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
user_input = input("Guess a Letter: ").upper()
if user_input in alphabet - used_letters:
    used_letters.add(user_input)
    if user_input in alphabet - used_letters:
        word.letters.remove(user_input)
        
elif user_input in alphabet - used_letters:
    print("You have already used that character. Please try again.")
print(user_input)


