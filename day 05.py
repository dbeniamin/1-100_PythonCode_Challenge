fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# EXERCISE NO.1 average height using for loop ( without using len / sum )
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")

number_students = 0
for student in student_heights:
    number_students += 1
print(f"number of students = {number_students}")

average_height = round(total_height / number_students)
print(f"average height = {average_height}")

# EXERCISE NO.2 - High Score using for loop
# Input a list of scores
student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
# defining the high score as 0
high_score = 0
for score in student_scores:
    # compare the high score defined against the scores in the list
    if score > high_score:
        # keeping the highest value encountered and saving it in the highscore variable
        high_score = score

print(f"The Highest score in the Class is: {high_score}")

# range will not take the large number entered as a limit
# using "," in the range definition is defining the step ie: range(1 , 12, 3) -> step 3


# EXERCISE NO.3 - Sum of even numbers up to an input
target = int(input())  # Enter a number between 0 and 1000
even_sum = 0
# start from 2 , adding 1 to the end and increment it by 2 meaning 
# adding 2 each time to the number to get the even numbers, for odd numbers start at 1
for number in range(2, target + 1, 2):
    # using += to add all numbers that respect the range defined
    even_sum += number
print(even_sum)

# EXERCISE NO. 4 - Fizz Buzz Game - Rules of the game
# if a number is cleanly divided by 5 print Buzz
# if a number is cleanly divided by 3 print Fizz
# if a number is cleanly divided by 5 and 3 print Fizz Buzz

# setting a target number - i.e. the upper limit of list to be looped through
target = 100
for number in range(1, target + 1):
    # cleanly divided by 3 and cleanly divided by 5
    # order matters in if statements so the most complex goes first
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# EXERCISE NO. 5 - Random Pass generator
# importing random and creating lists with all possible characters

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# new variable for each randomizing requested input
pass_letters = random.sample(letters, nr_letters)
pass_symbols = random.sample(symbols, nr_symbols)
pass_numbers = random.sample(numbers, nr_numbers)

# making 1 list
test1_pass = pass_letters + pass_symbols + pass_numbers
# test print to see if it works
# print(test1_pass)
# randomize the list
random.shuffle(test1_pass)
# test print to see if it works
# print(test1_pass)
# make the list a string and add a return a message
print(f"Here is your Password: " + "".join(test1_pass))
