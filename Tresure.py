print("Program for a game using logical operators and if conditions")
print("Welcome to Tresure Island\nYour mission is to find the tresure.")
direction = (input("You are at a cross road, where do you want to go ? Type 'left' or 'right' ")).lower()
'''if direction == "right":
    print("Game Over")
else:
    swim_or_wait = (input("Type 'swim' or type 'wait'")).lower()
    if swim_or_wait == "swim":
        print("Game Over")
    else:
        door = (input ("Which door do you want to go? type 'red', 'blue' or 'yellow' ")).lower()
        if door == "red" or door == "blue":
            print("Game Over")
        else:
            print("You win!")'''

if direction == "left":
    swim_or_wait = (input("type 'swim or 'wait' ? :")).lower()
    if swim_or_wait == "wait" :
        door = input("type 'red','blue' or 'yellow' : ")
        if door == "yellow":
            print("You win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game Over")