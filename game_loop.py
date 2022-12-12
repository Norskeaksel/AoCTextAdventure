import os
import sys

from GameFunctions.answer_mode import answer_mode
from GameFunctions.reset_game import reset_game
from GameFunctions.math_mode import math_mode
from GameFunctions.utils import player_has_won, victory_screen
from PrintFunctions.print_help import print_commands
from PrintFunctions.print_input import print_input
from PrintFunctions.print_status import print_status
from PrintFunctions.print_story import print_story
from PrintFunctions.print_task import select_task


def game_loop():
    while True:
        player_input = input().lower().strip()
        if player_input == "answer":
            answer_mode()
        elif player_input == "clear":
            os.system('cls')
        elif player_input == "help":
            print_commands()
        elif "input" in player_input:
            print_input(player_input)
        elif player_input == "math":
            math_mode()
        elif player_input == "reset":
            reset_game()
        elif player_input == "status":
            print_status()
        elif player_input == "story":
            print_story()
        elif "task" in player_input:
            select_task(player_input)
        elif player_input == "quit":
            print("So long, agent. See you next time.")
            sys.exit(0)
        elif player_input == "":
            pass
        elif '"' in player_input or "'" in player_input:
            print('Please do not use quotation marks in your commands')
        elif player_input == "victory":
            if player_has_won():
                victory_screen()
            else:
                print(player_input, 'is not a valid command\n'
                                    'Use the "help" command to list the commands at your disposal')

        else:
            print(player_input, 'is not a valid command\n'
                                'Use the "help" command to list the commands at your disposal')
