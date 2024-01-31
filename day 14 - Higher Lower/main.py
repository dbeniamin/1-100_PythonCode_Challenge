import random
import art
from game_data import data
import os

print(art.logo)


# format the data to printable

def stadium_format(stadium):
    # takes the data and returns printable format
    stadium_name = stadium["name"]
    return f"{stadium_name}"


def check_response(player_guess):
    stadium_a_capacity = stadium_a["capacity"]
    stadium_b_capacity = stadium_b["capacity"]
    # use the return , if guess is a return true if guess is not a return false
    if stadium_a_capacity > stadium_b_capacity:
        return player_guess == 'a'
    else:
        return player_guess == 'b'


score = 0
continue_game = True
stadium_b = random.choice(data)
stadium_a = random.choice(data)

while continue_game:

    # generate random entries from the list
    stadium_a = stadium_b
    stadium_b = random.choice(data)
    # in the slim case that the random module picks the same stadium
    while stadium_a == stadium_b:
        stadium_b = random.choice(data)

    print(f"Option A: {stadium_format(stadium_a)}")
    print(art.vs)
    print(f"Option B: {stadium_format(stadium_b)}")

    # asking the user to guess
    guess = input("What stadium has a higher capacity ? Type 'A' or 'B': ").lower()
    a_capacity = stadium_a["capacity"]
    b_capacity = stadium_b["capacity"]

    is_correct = check_response(guess)
    # check if user is corect
    os.system('cls||clear')

    if is_correct:
        score += 1
        print(f"You are right ! Current score: {score}")
    else:
        continue_game = False
        print(f"Wrong Answer !! Final Score {score}")
