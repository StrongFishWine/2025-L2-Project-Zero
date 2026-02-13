def not_blank(question):
    """makes sure user response isnt blank"""

    while True:
        response = input(question)

        if response != "":
            return response
        print("Sorry, this can't be blank. Please tey again.\n")


# main routire starts somewhere here
who = not_blank("Please enter your name: ")
print(f"Hello {who}")