print("Program for calculating the BMI using loop in the program")
weight = input(" Enter your weight : ")
height = input(" Enter your height : ")
bmi = (float(weight))/((float(height))**2)
if bmi < 35:
    if bmi <18.5:
        print(f"Your BMI is {bmi}, you are underweight")
    elif bmi>18.5 and bmi<25:
        print(f"Your BMI is {bmi}, You are normal weight")
    elif bmi>25 and bmi <30:
        print(f"Your BMI is {bmi},You are slightly overweight")
    else:
        print(f"Your BMI is {bmi},You are obese")
else:
    print(f"Your BMI is {bmi},You are clinically obese")