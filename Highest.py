print("Program for finding the highest score among the list")
score = input("Enter the scores : \n").split(",")
for n in range(0,len(score)):
    score[n] = int(score[n])
high = 0;
for n in score:
    if n>high:
        high = n
print(f"The highest score in the class is {high}")
