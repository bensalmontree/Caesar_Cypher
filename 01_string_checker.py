# Function goes here
def string_check(choice,options):
    for var_list in options:
        # If input is in one of the lists, return the full function
        if choice in var_list:
            # Get full name from list and convert to lowercase
            chosen=var_list[0].title()
            is_valid="yes"
            break
        # If the chosen option is not valid, set is_valid to no
        else:
            is_valid="no"
        # If the input is not OK - ask questions again.
    
    if is_valid=="yes":
        print("You chose " + chosen)
        return chosen
    else:
        print("Please enter a valid option")
        return "invalid choice"

# Valid responses 
cipher_list = ["encrpyt", "encryption", "decrypt", "decryption"]

# Create while loop for testing 
repeat = int(input("(Testing purposes) - Loop #: "))
while repeat >= 1:
    
    # Get input
    get_cypher = input("Encrypt or decrypt: ")
    get_cipher = string_check(get_cypher, cipher_list)
    repeat -= 1