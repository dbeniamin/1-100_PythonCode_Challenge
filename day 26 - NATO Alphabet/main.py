import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)

phonetic_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
# print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word: ").upper()
result_list = [phonetic_dict[letter] for letter in user_word]

print(result_list)
