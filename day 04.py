# Mersenne twister is the pseudorandom number generator used by python
# random module

import random

# randint(a, b) -> Returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.
random_integer = random.randint(1, 111)
print(random_integer)

# random.random() -> Returns a random floating point number between [0.0 to 1.0) - not including 1
# increasing the rage from 1 to X can be done by multiplying the value by X i.e to 5
random_float = random.random() * 5
print(random_float)

# EXERCISE NO. 1 - Coin Toss
# import random

coin_side = random.randint(0, 1)
# comparing and assigning Heads / Tails to each outcome.
if coin_side == 0:
    print("Heads")
else:
    print("Tails")

# LISTS are defined by ["item1", "item2, etc"] stored inside
# indexing items in lists starts from 0 !!!
# https://docs.python.org/3/tutorial/datastructures.html

states_of_romania = ["maramures", "bistrita", "salaj", "ilfov", "etc"]
# -1 is the last item of the list 
print(states_of_romania[-1])
# editing a specific item on the list
states_of_romania[0] = "Maramures"
# .append -> can be used to add an item at the end of the list
states_of_romania.append("Benjamins")

print(states_of_romania)

# EXERCISE NO. 2 - Random bill payer selector
# import random

names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(", ")
a = len(names)
# len() numbering starts from 1 so len of a 3 item list is 3 (1-2-3) while list indexing is 2 (0-1-2)
result = random.randint(1, a)
winner = names[result - 1]
print(f"{winner} is going to buy the meal today!")

# combining a lists 
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
# printing from second list the item with index 1
print(dirty_dozen[1][1])

# EXERCISE NO. 3 - Treasure Map

line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]

map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure?

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")

# EXERCISE NO.4 Rock Paper Scissor
# import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

test_images = [rock, paper, scissors]
user_choice = int(input("What do you Chose ? Please type 0 for Rock , 1 for Paper and 2 for Scissors\n"))

if user_choice >= 3 or user_choice < 0:
    print("Wrong number ! You Lost!!")
else:
    print(test_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer Chose")

    print(test_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win !!")
    elif computer_choice == 0 and user_choice == 2:
        print("Your LOST !!")
    elif computer_choice > user_choice:
        print("You Lost!!")
    elif user_choice > computer_choice:
        print("You Win !!")
    elif computer_choice == user_choice:
        print("It's a Draw")
