print("Program for a game 'Rock paper and Scissor' ")
import random
user_choice = (input("Enter your choice : Rock, Paper or Scissor : \n")).lower()
choice_1 = random.randint(0,2)
list = ['rock', 'paper', 'scissor']
computer_choice = list[choice_1]
print(f" You chose {user_choice}")
print(f" Computer chose {computer_choice}")
if user_choice == computer_choice:
    print("Draw")
elif user_choice == "rock" and computer_choice == "scissor":
    print("Rock wins against Scissor , You win!!!")
elif user_choice == "rock" and computer_choice == "paper":
    print("Paper wins against Rock , Computer win")
elif user_choice == "scissor" and computer_choice == "rock":
    print("Rock wins against Scissor , Computer win")
elif user_choice == "scissor" and computer_choice == "paper":
    print("Scissor win against Paper , You win!!!")
elif user_choice == "paper" and computer_choice == "rock":
    print("Paper wins against Rock , You win!!!")
elif user_choice == "paper" and computer_choice == "scissor":
    print("Scissor win against Paper , Computer win!!!")
else:
    print("Invalid")

