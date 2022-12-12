import json

from GameFunctions.utils import my_hash, open_file, solved_puzzles, player_has_won, victory_screen


def answer_mode():
    print("Entering answer mode. To escape, enter a non number, or a correct solution.\n"
          "You can right click to paste from your clipboard into the terminal")
    encrypted_solutions = json.load(open_file("_AoCEncryptedSolutions.json", "r"))
    player_answers = open_file("_PlayerAnswers.txt", "r").read().splitlines()

    while True:
        answer = input(": ").strip()
        try:
            int(answer)
        except ValueError:
            print(answer, "is not a number. Exiting answer mode.")
            break

        for puzzle, solution in encrypted_solutions.items():
            if my_hash(answer) == solution:
                if answer in player_answers:
                    print(f"Yes, you have already found that the answer to {puzzle} is {answer}.")
                else:
                    player_answers_file = open_file("_PlayerAnswers.txt", "a")
                    player_answers_file.write(answer + "\n")
                    score = solved_puzzles()
                    encouragement = ["Good start", "Well done", "Good job", "Excellent", "Great job",
                                     "Fantastic", "Awesome", "Perfect", "Amazing", "Incredible", "That's it"]
                    print(f"{encouragement[score]}, that is correct! The answer to {puzzle} is {answer}!")

                if player_has_won():
                    victory_screen()

                return

        print(answer, "is unfortunately not the correct answer to any of the puzzles.")
