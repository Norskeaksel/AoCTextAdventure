from GameFunctions.utils import player_has_won


def print_commands():
    print("answer \t prepare to submit an answer to a puzzle\n"
          "clear \t clears the console. (Does only work if the game is played in the console and not in an IDE like "
          "PyCharm)\n"
          "help \t lists the commands you have at your disposal\n"
          "input x  selects the puzzle input for puzzle x. x = [1-5]\n"
          "math \t enters math mode to do basic arithmetic like 7*7. Escape by entering an invalid math expression\n"
          "reset \t clears all progress and shuts down the game\n"
          "status \t lists your answer status for each puzzle\n"
          "story \t repeats the briefing for your mission\n"
          "task x \t selects the puzzle you want to see. x = [1-5]\n"
          "quit \t quit the game")

    if player_has_won():
        print("victory  you have won the game. Congratulations!")
