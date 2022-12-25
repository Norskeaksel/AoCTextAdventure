from GameFunctions.utils import player_has_won


def print_story():
    print("We are facing a severe threat.\n"
          "It appears that someone within our organization clicked on a malicious link.\n"
          "As a result, a computer virus has infiltrated our systems and is trying to encrypt our files.\n"
          "If it succeeds, our development efforts will be set back weeks.\n"
          "However, it seems like the virus creator has laid behind tracks for how to negate the virus.\n"
          "We believe that the 10 answers to 5 selected Advent of Code puzzles can be combined into the key for "
          "decrypting all affected systems.\n"
          "Your mission, should you choose to accept it, is to improve your skills in programing, to become a "
          "legitimate non-noob, if you will, and provide us these answers!\n"
          "It will require you to open an instance of your favorite IDE, pasting our provided puzzle inputs into "
          "files, and coding up solutions to the problems.\n")

    if player_has_won():
        print("\nBut you already know all this. You provided the answers and saved the organization. Thank you for "
              "playing!")
