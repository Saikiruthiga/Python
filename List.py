print("Program for selecting a person from a list and who is going to pay the bill")
import random
name_string = input("Enter the name of the people : \n")
names = name_string.split(", ")
index = random.randint(0,len(names)-1)
print(index)
person = names[index]
print(f"{person} is going to pay the bill!!!")

