print("Program for calculating BMI")
height = input("Enter your height in m : ")
weight = input("Enter your weight in kg : ")
bmi = int(weight) / (float(height))**2
#print("Your bmi value is " , bmi)
print("Your bmi value is " + str(bmi))