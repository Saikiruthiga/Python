print("Program for password generator ")
import random
letters = (['a','b','c','d','e'])
numbers = ['0','1','2','3','4']
symbols = ['@','#','$','(',')']
n_letters = int(input("How many letters you want to have in your password? "))
n_numbers = int(input("How many numbers you want to have in your password? "))
n_symbols = int(input("How many numbers you want to have in your password? "))
password = ""
for n in range(1,n_letters+1):
    password +=random.choice(letters)
for n in range(1,n_numbers+1):
    password +=random.choice(numbers)
for n in range(1,n_symbols+1):
    password +=random.choice(symbols)
mylist = []
for n in password:
    mylist += n
random.shuffle(mylist)   #shuffle method available in list hence we convert string into list and again given as string output
password = ''.join(mylist)
print(password)

# mylist = []
# for n in range(0,n_letters):
#     rand_letter = random.randint(0,n_letters)
#     mylist.append(letters[rand_letter])
# for n in range(0,n_numbers):
#     rand_number = random.randint(0,n_numbers)
#     mylist.append(numbers[rand_number])
# for n in range(0,n_symbols):
#     rand_symbol = random.randint(0,n_symbols)
#     mylist.append(symbols[rand_symbol])
# random.shuffle(mylist)
# password = (''.join(mylist))
# print(password)


