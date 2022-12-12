import sys
import json
from GameFunctions.make_victory_screen import make_victory_screen


def first_digit(string):
    for char in string:
        if char.isdigit():
            return int(char)

    return 0


def check_if_input_has_valid_digit(player_input, task_or_input="task"):
    task_nr = first_digit(player_input)
    if task_nr < 1 or task_nr > 5:
        player_input = input(f"Which {task_or_input} do you want to display? [1-5] ")
        task_nr = first_digit(player_input)
        if task_nr < 1 or task_nr > 5:
            print(f"No valid {task_or_input} found.")
            return -1

    return task_nr


def my_hash(text):
    hash = 0
    for ch in text:
        hash = (hash * 281 ^ ord(ch) * 997) & 0xFFFFFFFF

    return hash


def open_file(path, mode):
    try:
        file_content = open(path, mode)
    except FileNotFoundError as e:
        print(e)
        print("Exiting game")
        sys.exit(1)

    return file_content


def solved_puzzles():
    status = get_status()
    solved_puzzled = 0
    for answer in status.values():
        if answer != "Unknown":
            solved_puzzled += 1

    return solved_puzzled


def victory_screen():
    if player_has_won():
        player_name = open("_PlayerName.txt", "r").read()
        print(f"You've done them all. You are amazing {player_name}, sincerely. "
              "You have unlocked the victory screen I made for you. "
              "You can see it with the new command 'victory'.")
        response = input("Would you like to see the victory screen? [y/n] ").strip().lower()
        if response == "y" or response == "yes":
            make_victory_screen()


def player_has_won():
    score = solved_puzzles()
    if score < 10:
        return False

    return True


def get_status():
    status = {
        "Puzzle_1a": "Unknown",
        "Puzzle_1b": "Unknown",
        "Puzzle_2a": "Unknown",
        "Puzzle_2b": "Unknown",
        "Puzzle_3a": "Unknown",
        "Puzzle_3b": "Unknown",
        "Puzzle_4a": "Unknown",
        "Puzzle_4b": "Unknown",
        "Puzzle_5a": "Unknown",
        "Puzzle_5b": "Unknown",
    }

    status = update_status(status)
    return status


def update_status(status):
    player_answers = open_file("_PlayerAnswers.txt", "r").read().splitlines()

    hash_to_answer = dict()
    for ans in player_answers:
        hashed = my_hash(ans)
        hash_to_answer[hashed] = ans
    encrypted_solutions = json.load(open_file("_AoCEncryptedSolutions.json", "r"))
    for puzzle, hashed_answer in encrypted_solutions.items():
        if hashed_answer in hash_to_answer.keys():
            status[puzzle] = hash_to_answer[hashed_answer]

    return status
