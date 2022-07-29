from pydoc import plain


shift_value = 3
plain_text = "Hello, World! 123"

ciphered_text = ""

for c in plain_text:

    if c.isalpha():
        c_unicode = ord(c) + shift_value
        new_c = chr(c_unicode)
        ciphered_text = ciphered_text + new_c

    else:
        ciphered_text += c

print("Shift = " + str(shift_value))
print("Input = " + plain_text)
print("Your ciphered text is: " + ciphered_text)