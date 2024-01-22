# Name of the variable tips:
# 1 - make it meaningful 
# 2 - don't use privileged Syntax
# 3 - never start a variable name with a number
# 4 - use "_" to separate the words in the name of the variable

# \n  -> starts a new line when printing the output.
print("Hello World \nHello World")

# string concatenation or adding 2 string and printing 1 string , use " " as empty string to add spaces.
print("Hello" + " " + "Benjamin")

# input - represents a prompt for the user.
print("Hello " + input("What is your name?"))

# printing the length of an input requested string
print(len(input("What is your name? ")))

# defining a variable and printing the length of the string from that variable
name = input("What is your name ? ")
length = len(name)
print(length)

# printing the switched around values that the user inputted to console
a = input("a: ")
b = input("b: ")

# you need to create a 3rd variable to store one of the previously defined values
c = a
a = b
b = c
# printing the alternate inputs, input "a" as "b" and input "b" as "a"
print("a: " + a)
print("b: " + b)

# Day 1 project Tasks - uses all covered principles
# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line:

print("Hello and Welcome to my Basic Name Project !!")
city = input("Please tell me in what City where you born ...\n")
pet_name = input("Please tell me the name of your favourite Pet ...\n")
response = city + " " + pet_name
print("The name you are looking for is " + response)
