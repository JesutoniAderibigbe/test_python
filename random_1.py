#Random Module

import random
# import my_module

# print(my_module.my_fav_name) 


random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

#random number that prints out head or tail
coin_flip = random.randint(0, 1)
input("Press enter to flip the coin")
if coin_flip == 1:
    print("Heads")
else:
    print("Tails")