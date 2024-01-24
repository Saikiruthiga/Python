print("Program for Head or Tail using random module")
import random
coin = random.randint(0,1)
print(coin)
if coin == 0:
    print("Tails")
else:
    print("Heads")