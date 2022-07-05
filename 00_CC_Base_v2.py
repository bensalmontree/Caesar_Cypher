# Functions go here
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

    error="Please enter an integer"

    valid=False
    while not valid:

        # Ask user for number and check it is valid
        try:
            response=int(input(question))
            return response
            
        except ValueError:
            print(error)

# Valid responses 
cipher_list = ["encrpyt", "encryption", "decrypt", "decryption"]

# Get inputs (EN / DECRYPTION, PLAIN TEXT, SHIFT)
get_cipher = choice_checker("Encrypt or decrypt: ", cipher_list, "Invalid response, try again")
plain_text = input("Enter text to be ciphered: ")
shift_value = int_check("Enter your key / shift_value: ")

