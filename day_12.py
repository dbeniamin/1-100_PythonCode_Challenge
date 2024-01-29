###### Scope ######

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


### Local SCOPE ###

def drink_potion():
    potion_str = 3
    print(potion_str)


drink_potion()
### will give an error because it is defined in the function and does not exist outside, it has Local SCOPE
# print(potion_str) 

# Global scope , available everywhere because it was defined outside a function i.e. player_hp
player_hp = 10


# mind the indentations when you call a function or when you create a variable in order to be available for use
def game():
    def drink_potion():
        # Local scope - defined and available only inside a function - ie. potion_str 
        potion_str = 3
        print(player_hp)

    drink_potion()


#### There is no Block Scope in python ####

game_level = 3
enemies = ["Skeleton", "Alien", "Zombie"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

### Avoid modify the global scope ###
### Global Scope ie. global variable ( that will never change ) => all upper case ###


#  ### EXERCISE No. 1 - Guess the number ###

#  ### Guess Game ###  #
import random

EASY_TURNS = 10
HARD_TURNS = 5


# make a function to guess
def check_guess(guess, answer, turns):
    """Check the answer and returns the number of turns remaining"""
    if guess > answer:
        print("The number is to High.")
        # using the return to subtract the turns passed
        return turns - 1
    elif guess < answer:
        print("Too low !")
        return turns - 1
    else:
        print(f"You got it. The answer was: {answer}")


# difficulty set function
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        # using the global vars to set the gme difficulty
        return EASY_TURNS
    else:
        return HARD_TURNS


# main game function loop
def game():
    print("Welcome to the Number Guessing Game !")
    print("I'm thiking of a number between 1 and 100.")
    answer = random.randint(1, 100)

    # defining turns as equal to the previouslly defined function
    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Guess a number: "))
        turns = check_guess(guess, answer, turns)
        if turns == 0:
            print(f"You run out of guesses, YOU lost !")
            return


game()
