
def make_statement(statement, decoration, linesc):
    """Emphasises heading by adding decoration
    at the start and end"""

    print (f"{decoration * 3} {statement} {decoration * 3}")


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
make_statement( "Proggraming is FUUN!?", "=", 3)
print()
make_statement( "is still FUUN!?", "👍*👍", 2)
print()
make_statement( "mojis in action", "👍😍👍", 1)
