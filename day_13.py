### Debugging ####

# Describe Problem
# range function will not work becaue the upper limit is not taken in consideration
# for this code to print that string either lower the value of i or increase the range by 1
def my_function():
  for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) # lists index goes from 0 , solution requires rand function to start from 0
print(dice_imgs[dice_num])

# Play Computer
# ### use 1994 as the input => error becuse equal to 1994 is not representet
# ### the statement can change to >= 1994 or =< 1994
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# Fix the Errors
### indentation of print statement
### conversion from str to int not done and cant be added to print statement
### print statement needs a f to be a formated string in order to pass {age}
age = int(input("How old are you?"))
if age > 18:
print("You can drive at age {age}.")

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
### == means it will be eavaluated , = means it will assign the new value
### print word_per_page to see if the entered variable is assigned
print(word_per_page)
total_words = pages * word_per_page
print(total_words)

#### Use a Debugger
# b_list.append - indentation missmatch because it will catch only the last item of the list.
# b_list.append - same indetation as new_item is required so it will add all items to the empty list.
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])