import os
import sys


def reset_game():
    confirmation = input("Are you sure you want to reset the game? All progress will be deleted [y/n] ")
    if confirmation == "y":
        try:
            os.remove("_PlayerName.txt")
            os.remove("_PlayerAnswers.txt")
            print("All progress has been deleted. Restart the game to play again.")
        except FileNotFoundError as e:
            print(e)
            print("Could not find progress files. Exiting the game")

        sys.exit(0)

    else:
        print("That's good to hear")
