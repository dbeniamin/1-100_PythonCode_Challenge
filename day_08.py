# Functions

# def my_function():
#     do this
#     than do this
#     finally do this

# EXERCISE NO.1
# create a function -> 3 print statements -> call the function

def greet():
    print("Coding Challange")
    print("is going")
    print("very nice tbh!")


greet()


# Functions with Inputs

# def my_function(something that is the name of the variable):
#     do this with something
#     than do this
#     finally do

def greet_with_name(name):
    print(f"Hey {name} how is")
    print("the coding challange")
    print("going ?")


greet_with_name("Benjamin")


# name = Benjamin for the above example where name -> Parameter and "Benjamin" -> armugment

# Function with more than 1 input
def greet_with(name, location):
    print(f"Hey {name} how is it going?")
    print(f"What is your opinion about {location} ?")
    print("Is it sunny?")


greet_with("Benjamin", "Bucharest")


# # Positional Arguments -> a=1 , b=2 , c=3
# def my_function(a, b, c):
#     do this with a
#     than do this b
#     finally do this c

# # Keyword Arguments 
# def my_function(a, b, c):
#     do this with a
#     than do this b
#     finally do this c
# my_function(a = 1, b = 2, c = 3) -> if the order is changed (c = 3, a = 1, b = 2) -> it will keep the values.

def greet_with(name, location):
    print(f"Hey {name} how is it going?")
    print(f"What is your opinion about {location} ?")
    print("Is it sunny?")


greet_with(location="knitting water", name="does not matter")


# EXERCISE NO. 2 - Paint coverage calculator

def paint_calc(height, width, cover):
    # rounding up using the fact that // rounds down -> do the division on the negative number, then negate the answer.
    number_cans = -(-(height * width) // cover)
    print(f"You'll need {number_cans} cans of paint.")


test_h = int(input("Type the height of the wall in m: "))
test_w = int(input("Type the width3 of the wall in m: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# EXERCISE NO. 3 - Prime number check

def prime_checker(number):
    # creeating a variable that is true so it can compare if a number is prime
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            # if the conditions are meet, change the variable from true to false
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input())  # Check this number
prime_checker(number=n)

# Day 08 project - Cesar Cypher
