############### Blackjack Project #####################
############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

# Create deal_card() function that uses the List to *return* a random card, 11 is the Ace.
import random
import os
import art


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Create a function calculate_score() that takes a List as input and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(cards):
    # Inside calculate_score() check for a blackjack ->0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Inside calculate_score() check for an 11. If the score is already over 21, remove the 11 and replace it with a 1.
    if 11 in cards and sum(cards) > 21:
        # Remove the 11 .remove , and add 1 .append
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lost !"

    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "You Lost, A.i. has Blackjack !"
    elif user_score == 0:
        return "Won with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lost !"
    elif computer_score > 21:
        return "A.i. went over. You won!"
    elif user_score > computer_score:
        return "You won!"
    else:
        return "You lost!"


def play_game():
    print(art.logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        # adding computer and user cards
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user if they want to draw another card. If yes, then use the deal_card() function to add
            # another card to the user_cards List. If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it
    # has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls||clear')
    play_game()
