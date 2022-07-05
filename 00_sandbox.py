def casear_cipher(letter, num):
    """This function acts like a Casear Cipher. 

    Replaces an input letter with another letter a fixed
    number of spaces farther down the alphabet

    Args:
    * letter (string) - any upper case or lower case letter
    * num (integer) - any integer value to shift to a new letter"""

    if letter.isupper():
        starting_ascii = ord('A')
    elif letter.islower():
        starting_ascii = ord('a')
    else:
        raise ValueError('Input is not a letter')

    alpha_index = ord(letter) - starting_ascii
    mod_26 = (alpha_index + num) % 26
    return chr(starting_ascii + mod_26)

letter = "Hello"
num = 3

print("Encryption = " + casear_cipher(letter, num))