print("Program for finding the average height using 'for loop'")
stud_height = input("Enter the height of the students : \n").split(",")
for n in range(0, len(stud_height)):
    stud_height[n] = int(stud_height[n])
total_height = 0
for height in stud_height:
    total_height += height
num_of_stud = 0
for n in stud_height:
    num_of_stud = num_of_stud + 1
average_height = total_height / num_of_stud
print(f"The average_height is {average_height}")
# We can direcltly use sum() and len() function