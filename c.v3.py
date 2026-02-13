
def make_statement(statement, decoration, lines):
    """Emphasises heading by adding decoration
    at the start and end"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)

    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)

#main Routine goes here
make_statement( "Proggraming is FUUN!?", "*", 3)
print()
make_statement( "Is still FUUN!?", "=", 3)
print()
make_statement( "Mojis in action", "I", 3)
print()
