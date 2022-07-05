# Define Input
shift_value = 3
plain_text = "Hello, World! 123"

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
    x = ord(c) - starting_ascii

    # Perform shift
    en = (x + shift_value) % 26
    final_output = chr(starting_ascii + en)

    # Append to string
    ciphered_text = ciphered_text + final_output

# Output
print("Ciphered Text: " + ciphered_text)

# Expected Output: Khoor, Zruog! 123