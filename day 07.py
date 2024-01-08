# Hangman project 

# Step 1
import random

word_list = ["ardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# use random.choice to choose a random element and assign it to a new variable
chosen_word = random.choice(word_list)

print(chosen_word)

guess = input("Please guess a letter !!").lower()

# loop to check if letter in the chosen word match with input letter
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

# Step 2
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if
#  the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
#  guess.

guess = input("Guess a letter: ").lower()
count_letters = len(chosen_word)
print(count_letters)

display = []
for letter in chosen_word:
    # display.append("_") is the same with display += "_" -> adding an element to the list for each letter the word has
    display.append("_")
print(display)

# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter
#  replace with "_". Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)

# Step 3
import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the
#  letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
#  creating a variable to have a condition for the while loop
end_game = False

while not end_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)
    # checking if the conditions are meet to switch the variable state and end the while loop
    if "_" not in display:
        end_game = True
        print("You Won")

# Step 4
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

lives = 6

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # TODO-2: - If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        # if the letter is not in the word reduce the number of lives by 1
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lost !!")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has
    #  remaining.
    print(stages[lives])
