def encryption(plain_text,shift_value):
    
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

# Input     
plain_text = "Hello, World! 123"
shift_value = 3

# Output
print("Cipher: " + encryption(plain_text, shift_value))

# Expected Output: Khoor, Zruog! 123