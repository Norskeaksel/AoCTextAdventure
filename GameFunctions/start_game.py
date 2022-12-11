import os
from GameFunctions.utils import player_has_won
from PrintFunctions.print_story import print_story


def ask_player_to_start_game():
    if not os.path.exists('_PlayerAnswers.txt'):
        open('_PlayerAnswers.txt', 'w').close()
    try:
        player_name = open("_PlayerName.txt", "r").read()
        if player_name == "":
            raise FileNotFoundError
        welcome = "Are you ready to continue your mission?"
        if player_has_won():
            welcome = "You have won the game. Do you want to keep playing?"
        player_answer = input(f"Welcome back, agent. {welcome} [y/n] ").lower().strip()
    except FileNotFoundError:
        player_name = get_valid_player_name()
        print(f"Welcome, agent {player_name}.")
        print_story()
        player_answer = input("Do you accept this mission? [y/n] ").lower().strip()
        if player_answer == "y" or player_answer == "yes":
            save_player_name_to_file(player_name)

    return player_answer


def save_player_name_to_file(player_name):
    player_name_file = open("_PlayerName.txt", "w")
    player_name_file.write(player_name)
    player_name_file.close()


def get_valid_player_name():
    while True:
        player_name = input("What is your name? ").strip()
        if player_name == "":
            print("Bro, give us something to work with here")
            continue
        return player_name
