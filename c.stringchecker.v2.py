from c_yesandnosimple import yes_no


# functions here go
def string_check(question, valid_ans_list, num_letters):
    """checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # checks if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")


# Main routine here goes
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_check("Do you like coffee? ",
                           yes_no_list, 1)
print(f"You chose {like_coffee}")
pay_method = string_check( "Payment method: ", payment_list, 2)
print(f"You chose {pay_method}")