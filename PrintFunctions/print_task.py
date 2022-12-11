from GameFunctions.utils import check_if_input_has_valid_digit, open_file


def select_task(player_input):
    task_nr = check_if_input_has_valid_digit(player_input)
    if task_nr == -1:
        return

    path = "AoCPuzzleStatements/Puzzle"
    puzzle = open_file(path + f"{task_nr}.txt", "r")
    print("Task", task_nr, "selected")
    print(puzzle.read())

    print("To get the puzzle input for this task, enter input", task_nr)
    print("By selecting the input displayed in the console with the mouse and right clicking, "
          "it will be copied to the clipboard. \n"
          "You can then paste it into a file. Alternatively, you can look in the AoCPuzzleInput folder of the game "
          "and find it there.")
    print("Enter answer mode and submit your answer.")
