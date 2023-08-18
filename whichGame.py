# Importing random module.
import random

# Day 2 of learning Python off the Internet. 08/18/2023
# This is a program written to determine which game you should play today.
# Creates a list of game suggestions based on user input, to be randomized
suggestions = []
# Defining the function
def all_the_games(suggestions):   
    suggestions = []
    game1 = input("\nWhat should I play today?\nGive me a suggestion.\n")
    suggestions.append(game1)

# Asking for more suggestions
    more_games = input("\nWhat else wouldn't you mind playing tonight?\n")
    suggestions.append(more_games)
    print("\nHere's what we have so far.\n" + str(suggestions) +
          "\nShould we add some more?")
    game3 = input("\n'Yes' or 'No'\n")

# While loop, with yes/no conditionals
    while (game3.lower() == "yes"):
        more_games = input("\nWhat other game should we add?\n")
        suggestions.append(more_games)
        game3 = input("\nShould we add any more?\n'Yes' or 'No'\n")
        
# Randomizes index position once satisfied with the amount of games
    if (game3.lower() == "no"):
        print("\nAll right, here's what we have so far.\n" + str(suggestions))
        print("\nHere's a random game picked from what you've provided.\n")
        cap = int(len(suggestions))
        print(str(suggestions[random.randint(0, cap)]))
    else:
        print("\nIt's a 'Yes' or 'No' question.\n")
        print("Anyways, here are the games you've added.\n" + str(suggestions))
        print("\nHere's a random game picked from what you've provided.\n")
        cap = int(len(suggestions))
        print(str(suggestions[random.randint(0, cap)]))

# Calling the above function
all_the_games(suggestions)
