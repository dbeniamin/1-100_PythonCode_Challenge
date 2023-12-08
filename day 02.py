# Data Types
# String - "Hello" , any set of characters that is stored between "".
# Integer - numbers, using _ allows the user to better visualize large numbers.
# Float - number with decimals.
# Boolean - True or False.
# indexing (counting the position) starts from 0 in any list or string.

# using the [] allows the user to select what character from that string to be printed.
print("Hello"[4])

# will print the sum of 1234 + 5678
print(123_4 + 567_8)

num_char = len(input("What is my name ... ?"))
# converting the variable type from integer to string
# defining new variable that can be used to receive the output
new_conversion = str(num_char)
# adding the same data type
print("My name has " + new_conversion + " characters.")

# converting the 100.5 string in to a float -> adding 70 -> printing the result
print(70 + float("100.5"))

# converting 70 in to string -> converting 100 in to string -> concatenating the two strings -> printing the result
print(str(70) + str(100))

# Exercise no. 1 -> adding the 3 digits of a randomly inputted number
number_user = input("Type a three digit number: ")
# finding the type of the input
print(type(number_user))
# converting the digits input to integer
first_digit = int(number_user[0])
second_digit = int(number_user[1])
third_digit = int(number_user[2])
# adding the digits after conversion
sum_digits = first_digit + second_digit + third_digit
# printing the result
print(sum_digits)

# using the / operator will return a float type result even if the operation is clean
print(6 / 3)

# using the ** raises the power ->2 to the power of 6 
print(2 ** 6)

# THE RULE used to do math operations is PEMDAS = ( ) -> ** -> * / -> + -
# PEMDAS = Parentheses -> Exponents -> Multiplication -> Division -> Addition -> Subtraction

print(3 * 3 + 3 / 3 - 3)

# Exercise no.2 -> BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# converting data type to do the required calculations
height_user = float(height)
weight_user = int(weight)
result_bmi = weight_user / (height_user ** 2)
# converting is done while writing the formula
result = int(weight) / float(height) ** 2
# converting the result from float to int
bmi = int(result)
print(bmi)

# Rounding numbers
# round ( operation , number of decimals to be rounded)
print(round(8 / 3, 2))

# using // will convert the result to an integer and round it down
print(8 // 3)

# using += takes the previous version and adds 1 , can be used for all math operations
score = 0
score += 1
print(score)

# Formatted string
score = 0
height = 1.8
isWining = True
# f-String -> formatted string , converts all data types
print(f"the score is {score}, your height is {height}, you are winning is{isWining}")

# Exercise no. 3 -> Calculating Days / Weeks / months left until age 90
age = input("What is your current age? ")
user_input = int(age)
total_days = int(90 * 365)
total_weeks = int(90 * 52)
total_months = int(90 * 12)
user_days = user_input * 365
user_weeks = user_input * 52
user_months = user_input * 12
days_left = total_days - user_days
weeks_left = total_weeks - user_weeks
months_left = total_months - user_months

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months left.")

# Exercise no. 4 -> Tip calculator
print("Welcome to the Tip Calculator !")
total_bill = input("What was the total bill ? $")
# converting to float so it's easy to do math with it
bill = float(total_bill)
tip_option = input("What percentage tip would you like to give ? 10, 12, or 15 ?")
# calculating the value of the tip based on the chosen percent
tip = float((bill * int(tip_option)) / 100)
people_total = input("How many people are splitting the bill ?")
# converting to int, so we can use it to do math
people = int(people_total)
# calculating the total that needs to be paid by each person.
totals = ((tip + bill) / people)
# rounding the result to show only 2 decimals
result = float(round(totals, 2))
# formatting the result to display 2 decimals even if the last decimal is 0
# if the last decimal is 0 python will not show it without proper formatting
result_final = "{:.2f}".format(result)
print(f"Each person should pay: $ {result_final} ")
