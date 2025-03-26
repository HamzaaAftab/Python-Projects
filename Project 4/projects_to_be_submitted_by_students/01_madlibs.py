
################################ EXPLAINING OF THE PROJECT #################################
# # String Concatenation means how to put Strings together or combine them
# # There are several ways to do this in Python

# youtuber = "Hamza" 

# # Simple Method
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber)) # What this will do? this will simply put the value of Youtuber into {} using .format()
# # Now the most famous and common method in python to do this is using F strings
# print(f"Subscribe to {youtuber}") # This is called formatted string literals or f-strings in python


adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because \n I love to {verb1}. Stay Hydrated and {verb2} like you are {famous_person}..!  "

print(madlib)