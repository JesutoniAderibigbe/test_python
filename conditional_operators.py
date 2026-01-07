#conditional operators

print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")


#check if the user input is odd or even
isEven = int(input("Enter a number to check if it's odd or even: "))
if isEven % 2 == 0:
  print("This is an Even number")
else:
   print("Sorry this is an odd number")
    

# Multiple If Statemenets in Succession
num = int(input("Enter a number: "))
if num > 0:
    print(num, "is a positive number")
if num == 0:
    print(num, "is zero")
if num < 0:
    print(num, "is a negative number")
# Nested If Statements
num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print(num, "is zero")
    else:
        print(num, "is a positive number")
else:
    print(num, "is a negative number")



    #task creating a pizza order practice
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25  

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


#Building a Treasure Island Game
print("Welcome to Treasure Island.")

print("Your mission is to find the treasure.")

choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()

if choice1 == "left":
    choice2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    else:
        print("You get attacked by an angry trout. Game Over.")

else:
    print("You fell into a hole. Game Over.")


