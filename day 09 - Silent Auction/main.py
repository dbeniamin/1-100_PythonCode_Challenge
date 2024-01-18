import os
import art

# comand used to clear the screen in VS code after importing the os module
# os.system('cls||clear')

print(art.logo)

# create empty dictionary to store the names and bids
bids = {}
# making a value to keep track if the bidding is done or not
bidding_done = False


def highest_bidder(bidding_record):
    # making a value high bid to start comparing
    highest_bid = 0
    # making a bidder name variable 
    winner = ""
    for bidder in bidding_record:

        # getting the value based on the key stored in the dictionary
        bid_ammount = bidding_record[bidder]

        # compare the bid value with the highest bid that starts at 0
        if bid_ammount > highest_bid:
            # store the highest value goten from dictionary as the highest_bid
            highest_bid = bid_ammount
            # getting the winner names based on the dictionary key - bidder_name stored as bidder
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_done:
    # variables that will take the input 
    bidder_name = input("Please tell me your name ...\n")
    # making the input integer in order to compare
    price = int(input("Please place your bid: $"))

    # adding to the dictionary 
    # empty dictionary created [key i.e. bidder_name] = value -> i.e. price
    bids[bidder_name] = price
    # variable that stores if there are more bids
    continue_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    # break the loop and chage the status of continue_bids presiouslly set
    if continue_bids == "no":
        bidding_done = True
        highest_bidder(bids)
    elif continue_bids == "yes":
        os.system('cls||clear')
