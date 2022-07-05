shift_value = 5
plain_text = "UFXX\TWI6789:"

ciphered_text = ""

for c in plain_text:

    if c.isalpha() or c.isnumeric():
        c_unicode = ord(c) - shift_value
        new_c = chr(c_unicode)
        ciphered_text = ciphered_text + new_c

    else:
        ciphered_text += c

print("Your ciphered text is: " + ciphered_text)