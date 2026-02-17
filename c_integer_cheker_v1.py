
# Functions here
def int_check(question):
    """Checks users enter an integer that is more than zero (or the 'xxx' exit code)"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)

# Main Routine goes here

# loop for testing purposes........
while True:
    print()

    # ask user for their name
    name = input("Name: ") # replace with call to 'not blank' function!

    # ask user for their age and checks it's between 12 and 120
    age = int_check("Age: ")

    # Ask error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")