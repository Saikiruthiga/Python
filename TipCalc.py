print("Program for calculating the bill")
print("Welcome to the tip calculator")
bill = input("What was the total bill? : ")
tip = input("What percent tip would you like to give? 10 ,12 or 15 : ")
num_of_persons = input("How many people to split hte bill? : ")
amount = ((float(bill) * (float(tip) / 100)) + float(bill) ) / int(num_of_persons)
# total = round(amount,2)
print(f"Each person should pay : {round(amount,2)}")