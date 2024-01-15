# import art

# print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# adding modulo 26
# i.e. number of letters in alphabet
#  to reduce the shift if the user enters a number > 26
# shift = shift % 26

def caesar(text, direction, shift_amount):
    code_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
            code_text += alphabet[new_position]
            # print(f"The encoded text is {code_text}")

        else:  # direction == "decode"
            new_position = position - shift_amount
            code_text += alphabet[new_position]
            # print(f"The decoded text is {code_text}")
    # using the direction as an argument for a formated string to get the options for the user
    # used outside if / else block so you don't have multiple outputs printed on the console
    print(f"The {direction}ed text is ->{code_text}<-")


caesar(text, direction, shift_amount=shift)
