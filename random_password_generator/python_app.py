# Ask user if they want to genereate a password or not 
# If yes, ask for password length
# Generete password
# Print Password
# If initial response is no, exit program

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#£$%^&*()")


def generete_password():
    password_length = int(input("How long would you like your password to be? "))
    random.shuffle(characters)

    password = []

    for x in range(password_length): 
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    

    print(password)


option = input("Do you want to generate a password? (Y/N) ") 


if option.lower() == "y": 
    generete_password()
elif option.lower() == "n": 
    print("Program Ended")
    quit()
else: 
    print("Invalid input, please input Y or N ")
    quit()




