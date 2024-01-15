alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd',
            'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# make the function with new arguments that will be defined when called
def encrypt(plain_text, shift_number):
    # creeate an empty string
    cipher_text = ""

    # make for loop, so it will check in the original list ie. alphabet
    for letter in plain_text:
        # getting the index for letters in the original list
        # .index will give the index for the first encoutered item in the list
        #  ie. a will get index 0 and the function will stop even if we have 'a' 2 times
        position = alphabet.index(letter)

        # shifting indexes using the shift number
        # if at the end of the list, duplicating the list will make a loop
        new_position = position + shift_number

        # getting the index of new letters in the list
        new_letter = alphabet[new_position]

        # adding the new letters to get the coded message
        cipher_text += new_letter

    # indenting the print inside the for loop
    # prints the new string stept by step with new values
    print(f"Encoded message is {cipher_text}")


# calling the function and passing arguments to use the input provided
# encrypt(plain_text = text, shift_number = shift)

def decrypt(cipher_text, shift_number):
    # creeate an empty string
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_number
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"Orginal message is {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_number=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_number=shift)
