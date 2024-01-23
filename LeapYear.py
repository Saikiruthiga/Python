print("Program to find given year is leap year or not")
year = int( input("Enter a year"))
if (year % 4 ==0 ) :
    if (year % 100 == 0) :
        if (year % 400 == 0) :
            print(f"The given year {year} is a leap year")
        else:
            print(f"The given year {year} is a non-leap year")
    else:
        print(f"The given year {year} is a leap year")
else:
    print(f"The given year {year} is a non-leap year")