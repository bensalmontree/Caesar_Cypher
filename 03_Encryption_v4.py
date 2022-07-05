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

# Create while loop for testing 
repeat = int(input("(Testing purposes) - Loop #: "))
while repeat >= 1:

    # Input     
    plain_text = input("Plain Text: ")
    shift_value = int(input("Shift: "))

    # Output
    print("Cipher: " + encryption(plain_text, shift_value))
    print()
    repeat -= 1

# Expected Output: Khoor, Zruog! 123
