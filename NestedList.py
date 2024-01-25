print("Program for mark 'X' in a given matrix using nesterd list")
line_1 = [" ", " ", " "]
line_2 = [" ", " ", " "]
line_3 = [" ", " ", " "]
map = [line_1, line_2, line_3]
position = (input("Enter the value to mark 'X' ")).upper()
# if position[0] == 'A' and position[1] =='1':
#     map[0][0] = 'X'
# elif position[0] == 'A' and position[1] =='2':
#     map[1][0] = 'X'
# elif position[0] == 'A' and position[1] =='3':
#     map[2][0] = 'X'
# elif position[0] == 'B' and position[1] =='1':
#     map[0][1] = 'X'
# elif position[0] == 'B' and position[1] =='2':
#     map[1][1] = 'X'
# elif position[0] == 'B' and position[1] =='3':
#     map[2][1] = 'X'
# elif position[0] == 'C' and position[1] =='1':
#     map[0][2] = 'X'
# elif position[0] == 'C' and position[1] =='2':
#     map[1][2] = 'X'
# elif position[0] == 'C' and position[1] =='3':
#     map[2][2] = 'X'
# else:
#     print("Invalid input")
# print(f"{line_1} \n {line_2} \n {line_3}")


abc = ['A','B','C']
letter_index = abc.index(position[0])
number_index = (int(position[1])- 1)
map[number_index][letter_index] = 'X'
print(f"{line_1} \n {line_2} \n {line_3}")
