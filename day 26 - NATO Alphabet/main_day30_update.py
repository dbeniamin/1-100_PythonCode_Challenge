import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)

phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# creeate a func
# add try to the posible problem line
# define exception and pass the func again to run a loop unitl the user enters correct data
def generate_nato_alphabet():
    user_word = input("Enter a word: ").upper()

    try:
        result_list = [phonetic_dict[letter] for letter in user_word]

    except KeyError:
        print("Please enter only letters")
        # call the func again to be run in a loop as long as the exception is met
        generate_nato_alphabet()

    else:
        print(result_list)


generate_nato_alphabet()
