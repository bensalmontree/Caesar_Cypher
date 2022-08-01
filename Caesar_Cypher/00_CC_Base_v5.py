import random

# Functions go here
def cipher(plain_text, shift_value):

    ciphered_text = ""

    # If encrypting add shift, if decrypting remove
    if get_cipher == "encrypt":
        add_sub = "+"
    else:
        add_sub = "-"
    
    # For encryption use formula En(x) = (x + n)mod 26
    for c in plain_text:

        # Determine starting ascii for range using ord function
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
        new_index = eval(str(c_index) + add_sub + str(shift_value)) % 26

        # Convert to new character using chr function
        final_output = chr(starting_ascii + new_index)

        # Append to string
        ciphered_text += final_output

    return ciphered_text

# Checks if response is valid
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

# Checks for an integer, if no integer is inputted return random number between 1-10
def int_check(question):

    valid = False
    while not valid:

        if get_cipher == "encrypt":

            # Ask user for number and check it is valid
            try:
                response = int(input(question))
                return response

            # If no input, generate random number
            except ValueError:
                random_number = random.randint(1,25)
                print("Shift value is left blank, randomly generated shift: " + str(random_number))
                return random_number

        else:
            # Ask user for number and check it is valid
            try:
                response = int(input(question))
                return response

            # If decrypting and user does not have key, proceed to randomly generate possible  
            except ValueError:                
                hack = True
                print("Shift not found, generating list of possible solutions...")
                return hack

# Valid responses
cipher_list = ["encrypt", "encryption", "decrypt", "decryption"]
yes_no_list = ["yes", "no"]


# Start of loop
loop = "yes"
while loop == "yes":

    # Define shift_value
    shift_value = False

    # Get inputs (EN / DECRYPTION, PLAIN TEXT, SHIFT)
    get_cipher = choice_checker("Encrypt or decrypt: ", cipher_list, "Invalid response, try again")
    plain_text = input("Enter text to be ciphered: ")
    shift_value = int_check("Enter your key / shift_value: ")

    # Output
    if get_cipher == "encrypt":
        print("Cipher: " + cipher(plain_text, shift_value))

    else:

        # For decryption and key is unknown, iterate through every possible decryption key and generate list
        if shift_value == True:
            
            # Goes through all keys
            print()
            for i in range(0,26):
                brute_force_text = cipher(plain_text, i)
                print("Key #{}: {}".format(i, brute_force_text))

        else:
            print("Cipher: " + cipher(plain_text, shift_value))

    print()

    # Ask user if they want to continue loop
    loop = choice_checker("Do you have more code to cipher? ", yes_no_list, "Invalid response, try again")
