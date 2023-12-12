print("Welcome to the roller coaster!")
# converting the input string to an integer and store it in a variable
height = int(input("What is your height in cm ..? "))
# Comparison operators:
# == --> Equal To, != --> Not Equal To, <= --> Less Than or Equal, >= --> Greater Than or Equal
# = --> Means assigning the value to the variable
# == --> Checking the Equality (Value on the right is the same with the value on the left)
if height >= 120:
    print("You can ride !!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    # elif - can be used to add as many conditions as needed
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("You need to grow taller before you can ride.")

# EXERCISE NO. 1 find out if a given number is an odd or even number.
# converting to integer when the variable is defined to do further math
number = int(input("Which number do you want to check? "))
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
result = number % 2
# printing a defined variable you assigned to check yourself is a good idea
# print(result)

if result == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# EXERCISE NO.2 - BMI Calculator 2.0
# using the float to covert since most of the height is 1.XX
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# rounding the numbers so it wil chose the closes full number i.e. 22.4 -> 22 , 22.7 -> 23
bmi = round(weight / (height ** 2))

if bmi <= 18:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# EXERCISE NO.3 - a program that works out whether if a given year is a leap year.
# This is how you work out whether if a particular year is a leap year.
# 1 - on every year that is evenly divisible by 4 
# 2 - except every year that is evenly divisible by 100 
# 3 - unless the year is also evenly divisible by 400
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

# MULTIPLE IF (if all conditions are true - you get all executions)
# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do C

print("Welcome to the roller coaster!")

height = int(input("What is your height in cm ..? "))
bill = 0

if height >= 120:
    print("You can ride !!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        print("You are young at hearth. Have a free ride on us !")
    else:
        bill = 12
        print("Adult tickets are $12.")

    want_photo = input("Do you want a photo taken? Y or N\n")
    if want_photo == "Y":
        # (bill = bill + 3) is the same as (bill += 3)
        bill += 3
    print(f"Your total bill is ${bill}")

else:
    print("You need to grow taller before you can ride.")

# EXERCISE NO. 3 - an automatic pizza order program.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
        print(f"Your final bill is: ${bill}.")
    else:
        print(f"Your final bill is: ${bill}.")
else:
    print()

# EXERCISE NO.4 - Love score calculator
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2-digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")  # or adding the .lower() after the variable name definition
name2 = input("What is their name? \n")  # this will remove the need to redefine and convert de variable separate.
# turning the input to lower case strings
l_case1 = name1.lower()
l_case2 = name2.lower()
# counting the number of times each letter is in every string
l_true_1 = l_case1.count("t") + l_case1.count("r") + l_case1.count("u") + l_case1.count("e")
l_love_1 = l_case1.count("l") + l_case1.count("o") + l_case1.count("v") + l_case1.count("e")
l_true_2 = l_case2.count("t") + l_case2.count("r") + l_case2.count("u") + l_case2.count("e")
l_love_2 = l_case2.count("l") + l_case2.count("o") + l_case2.count("v") + l_case2.count("e")

# turning the numbers of letters repeat to string in order to concatenate
love_score = str(l_true_1 + l_true_2) + str(l_love_1 + l_love_2)

# turning the concatenated score to integer, so it can be compared to the conditions
score = int(love_score)

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

# EXERCISE NO.5 - Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_choice = input("Please choose if you want to go left or right ...\n").lower()

if first_choice == "left":
    #  setting up the next choice inside the if statement
    second_choice = input("You are in front a lake ... Do you Swim or Wait ...?\n").lower()
    if second_choice == "wait":
        third_choice = input("You are in front of the castle ... Do you go Up or Down ...\n").lower()
        if third_choice == "down":
            fourth_choice = input(
                "You are in front of three doors ... Do you chose the Red, Blue or Yellow ...\n").lower()
            if fourth_choice == "red":
                # using elif for multiple choice options
                print("Wrong choice !! Game over...")
            elif fourth_choice == "blue":
                print("Wrong choice !! Game over...")
            elif fourth_choice == "yellow":
                print("You Won !!")
            else:
                print("Wrong choice !! Game over...")
        else:
            print("Wrong choice !! Game over...")
    else:
        print("Wrong choice !! Game over...")
else:
    print("Wrong choice !! Game over...")
