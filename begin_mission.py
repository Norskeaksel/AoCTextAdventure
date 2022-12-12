import sys

from game_loop import game_loop
from GameFunctions.start_game import ask_player_to_start_game

player_answer = ask_player_to_start_game()
if player_answer not in ["y", "yes"]:
    print("Understandable. Have a nice day.")
    sys.exit()

print('Excellent! To progress, enter a valid command.\n'
      'Use the "help" command to list the commands you have at your disposal.')
game_loop()
