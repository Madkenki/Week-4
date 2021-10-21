# Instructions
# Demonstrates programmer-created functions

def instructioins():
    """Display game instructions."""
    print(
    """
    Welcome to python Tic-Tac-toe game.
    You will make your move known by entering a number, 0-8. The number will co0rrespond to the board position as illustrated:


                    0|1|2
                    -----
                    3|4|5
                    -----
                    6|7|8

    The game is about to start.\n
    """
    )

# main
print("Here are the instructions for the game:")
instructions()
print("Here they are again:")
instructions()
print("You probably understand the game by now.")

input("\n\npress the enter key to exit.")

def instructions():
