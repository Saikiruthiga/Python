print("Program for adding the even numbers using for loop and range")
target = int(input("Enter a value : \n"))
sum =0
for n in range(0,target+1,2):
    sum = sum +n
print(sum)