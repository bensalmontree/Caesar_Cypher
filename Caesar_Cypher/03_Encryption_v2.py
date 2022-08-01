# Define Input
shift_value = 3
plain_text = "Hello, World! 123"

ciphered_text = ""

# For encryption use formula En(x) = (x + n)mod 26
for c in plain_text:

    # For range of ASCII uppercase letters
    if ord(c) in range (65, 91):

        # Find position in unicode 
        x = ord(c) - ord('A')

        # Perform shift
        en = (x + shift_value) % 26
        final_output = chr(ord('A') + en)
    
        # Append to string
        ciphered_text = ciphered_text + final_output
    
    # For range of ASCII lowercase letters
    elif ord(c) in range (97, 123):

        # Find position in unicode 
        x = ord(c) - ord('a')

        # Perform shift
        en = (x + shift_value) % 26
        final_output = chr(ord('a') + en)

        # Append to string
        ciphered_text = ciphered_text + final_output

    # Excluding numbers, symbols, special characters, etc.
    else:
        ciphered_text += c

# Output
print("Shift: " + str(shift_value))
print("Plain Text: " + plain_text)
print("Ciphered Text: " + ciphered_text)

# Expected Output: Khoor, Zruog! 123