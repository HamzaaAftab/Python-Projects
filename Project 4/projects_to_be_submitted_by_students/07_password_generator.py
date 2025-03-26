import random

print("Welcome to Password Generator...!")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&1234567890./*'

number = int(input("Amout of passwords to generate : "))
number = int(number)

length = input("Input Your Password Length: ")
length = int(length)

print("\nHere are Your Passwords..")

for i in range(number):
    password = ''.join(random.choice(chars) for x in range(length))
    print(password)

