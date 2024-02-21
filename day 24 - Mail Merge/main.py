### Documentation References ###
# https://www.w3schools.com/python/ref_file_readlines.asp
# https://www.w3schools.com/python/ref_string_replace.asp
# https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

# use .readlines() to create a list of items with the names
with open("./Receivers/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)

with open("./Letter/start_template.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        # use strip method to remove the empty lines
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

