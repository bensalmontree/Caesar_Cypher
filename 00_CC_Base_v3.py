# Functions go here
def encryption(plain_text, shift_value):

    ciphered_text = ""

    # For encryption use formula En(x) = (x + n)mod 26
    for c in plain_text:

        # Determine starting ascii for range
        if c.isupper():
            starting_ascii = ord('A')

        elif c.islower():
            starting_ascii = ord('a')

        # Exclude encryption for numbers, symbols, etc.
        else:
            ciphered_text += c
            continue

        # Find position in unicode
        c_index = ord(c) - starting_ascii

        # Perform shift
        new_index = (c_index + shift_value) % 26

        # Convert to new character
        final_output = chr(starting_ascii + new_index)

        # Append to string
        ciphered_text = ciphered_text + final_output

    return ciphered_text

def decryption(plain_text, shift_value):

    ciphered_text = ""

    # For encryption use formula En(x) = (x + n)mod 26
    for c in plain_text:

        # Determine starting ascii for range
        if c.isupper():
            starting_ascii = ord('A')

        elif c.islower():
            starting_ascii = ord('a')

        # Exclude encryption for numbers, symbols, etc.
        else:
            ciphered_text += c
            continue

        # Find position in unicode
        c_index = ord(c) - starting_ascii

        # Perform shift
        new_index = (c_index - shift_value) % 26

        # Convert to new character
        final_output = chr(starting_ascii + new_index)

        # Append to string
        ciphered_text = ciphered_text + final_output

    return ciphered_text

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response is an item
        # in the list ( or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item is not in list
        print(error)
        print()

# Checks for an integer more than 0
def int_check(question):
    error = "Please enter an integer"

    valid = False
    while not valid:

        # Ask user for number and check it is valid
        try:
            response = int(input(question))
            return response

        except ValueError:
            print(error)

# Valid responses
cipher_list = ["encrypt", "encryption", "decrypt", "decryption"]
yes_no_list = ["yes", "no"]

# Start of loop
loop = "yes"
while loop == "yes":

    # Get inputs (EN / DECRYPTION, PLAIN TEXT, SHIFT)
    get_cipher = choice_checker("Encrypt or decrypt: ", cipher_list, "Invalid response, try again")
    plain_text = input("Enter text to be ciphered: ")
    shift_value = int_check("Enter your key / shift_value: ")

    # Output
    if get_cipher == "encrypt":
        print("Cipher: " + encryption(plain_text, shift_value))
        print()

    elif get_cipher == "decrypt":
        print("Cipher: " + decryption(plain_text, shift_value))
        print()
    
    else:
        break

    loop = choice_checker("Repeat? [y/n] ", yes_no_list, "Invalid response, try again")