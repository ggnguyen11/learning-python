# I caught myself going past the PEP8 character limit of 79 in my code, so I've
# decided I'd try to code a program to count the characters in any given line.
# Still day 2 of learning Python off the Internet. 08/18/2023
# Defining the function
def i_can_count():
# Was encountering SyntaxError because I didn't know how to properly line break
# when met with the 79 character limit in code itself. I remedied this by
# concatenating.
    line = input("Please paste the line of code you need counted." +
                 "\nSimply right click here to paste.\n")
# Message for lines above 79.
    if len(line) > 80:
        print("\nYou should line break, it's longer than 79" +
              " characters." + "\nOr, you know, write better code. ;)\n") 
# Length of object
    print("Character Length: " + str(len(line)))

# Calling the function above
i_can_count()