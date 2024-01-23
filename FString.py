print("Program for calculating the remaining weeks in our lifetime using 'fstring' ")
age = input("Enter your age : ")
weeks = (90*52)-(int(age) *52)
print(f"You have {weeks} weeks left")