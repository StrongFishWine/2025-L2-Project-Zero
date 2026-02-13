# functions here!!!
def yes_no(question):
    """Checks users use yes or no"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y" or response == "ok":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")


# Main routine goes here

#  loop for testing purposes...
while True:
    want_instructions = yes_no("Do you want to read the instructions? ")
    print(f"You chose {want_instructions}\n")
