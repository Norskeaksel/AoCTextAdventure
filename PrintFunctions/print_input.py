from GameFunctions.utils import check_if_input_has_valid_digit, open_file


def print_input(player_input):
    input_nr = check_if_input_has_valid_digit(player_input, "input")
    if input_nr == -1:
        return

    print("Input", input_nr, "selected")
    path = "AoCPuzzleInputs/Input"
    puzzle = open_file(path + f"{input_nr}.txt", "r")
    print(puzzle.read())




