# Checks for an integer more than 0
def int_check(question):
    error="Please enter an integer"
    valid=False
    while not valid:
        # Ask user for number and check it is valid
        try:
            response=int(input(question))
            print(response)
            return response
        except ValueError:
            print(error)


# Create while loop for testing 
repeat = int(input("(Testing purposes) - Loop #: "))
while repeat >= 1:

    shift_value = int_check("Enter your key / shift_value: ")
    repeat -= 1