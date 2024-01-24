print("Program for Logical operators")
name_1 = input("Enter the first name : ")
name_2 = input("Enter the second name : ")
new_name = (name_1 + name_2).lower()
count = new_name.count("t") + new_name.count("r") + new_name.count("u") + new_name.count("e")
count_1 = new_name.count("l") + new_name.count("o") +new_name.count("v") + new_name.count("e")
score = str(count) + str(count_1)
score_1 = int(score)
if(score_1 < 10 or score_1 > 90):
    print(f"Your score is {score} , you go together like coke and mentos")
elif(score_1 > 40 and score_1 < 50):
    print(f"Your score is {score_1}, you are alright together")
else:
    print(f"Your score is {score_1}")
