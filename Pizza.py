print("Program for ordering pizza using multiple if conditions")
print("Thank you for choosing python pizza deliveries!")
size = input("Enter the size of your pizza ? S, M or L : ")
pepperoni = input("want to add pepperoni ? Y or N :")
cheese = input(" Want to add extra cheese ? Y or N : ")
bill = 0
if size == "S":
    bill = bill + 15
    if pepperoni == "Y":
        bill = bill + 2
elif size == "M":
    bill = bill + 20
    if pepperoni == "Y":
        bill = bill + 3
elif size == "L":
    bill = bill + 25
    if pepperoni == "Y":
        bill = bill + 3
else:
    print("Invalid")
if cheese == "Y":
    bill = bill + 1
print(f"Your final bill is {bill}")