import random
exit = False
user_points = 0
computer_points = 0

options = ["rock", "paper", "scissors"]

while exit == False:
    user_input = input("Choose rock, paper, scissors or exit: ").lower()
    computer_input = random.choice(options)

    if user_input == "exit":
        print(" \n You won total score of "+ str(user_points) + " and the computer total score of "+ str(computer_points))

        if computer_points < user_points:
            print("You won!")
        elif computer_points > user_points:
            print("Computer wons!")
        else: 
            print("It is tie!")

        print("Game Ended")
        exit = True

    if user_input =="rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is tie!")
        elif computer_input =="paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer wins!")
            computer_points +=1
        elif computer_input =="scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("You win!")
            user_points +=1
    elif  user_input =="paper":
        if computer_input == "rock":
            print("Your input is paper")
            print("Computer input is rock")
            print("You Win!")
            user_points +=1
        elif computer_input =="paper":
            print("Your input is paper")
            print("Computer input is paper")
            print("It is tie")
           
        elif computer_input =="scissors":
            print("Your input is paper")
            print("Computer input is scissors")
            print("Computer wins!")
            computer_points +=1

    elif  user_input =="scissors":
        if computer_input == "rock":
            print("Your input is scissors")
            print("Computer input is rock")
            print("Computer Wins!")
            computer_points +=1
        elif computer_input =="paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You win!")
            user_points +=1
           
        elif computer_input =="scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It is tie")
    else:
        if user_input != "exit":
            print("Invalid value")

            











