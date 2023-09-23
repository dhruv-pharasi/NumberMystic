from random import randint
from os import system, path

print("\nWelcome to NumberMystic, a number guessing game.\n")


def setup():
    '''Sets the game based on user's chosen difficulty.'''
    ans = input("\nChoose a difficulty: 'easy', 'hard', or 'supreme'\n")

    # Setting number of attempts based on selected difficulty.
    if ans == "easy":
        attempts = 8
        read_art_file()
        start_game(attempts)

    elif ans == "hard":
        attempts = 4
        read_art_file()
        start_game(attempts)

    elif ans == "supreme":
        attempts = 6
        read_art_file()
        start_game(attempts)

    else:
        print("\nInvalid input\n")
        setup()


def start_game(attempts):
    '''Contains the game loop.'''

    # Generating a random number to be guessed by the player
    if attempts == 6:
        # For supreme difficulty
        to_guess = randint(1, 500)
        print("\nI'm thinking of a number between 1 and 500.")
        print(f"You have {attempts} attempts remaining to guess the number.")

    else:
        # For easy/hard difficulty
        to_guess = randint(1, 100)
        print("\nI'm thinking of a number between 1 and 100.")
        print(f"You have {attempts} attempts remaining to guess the number.")

    # A boolean flag to run the game loop
    not_guessed = True

    # Game runs till the player has attempts remaining and the number hasn't been guessed
    while attempts > 0 and not_guessed:
        player_guess = input("\nMake a guess: ")

        # Validating user input; it must be a number
        if not player_guess.isdigit():
            print("\nInvalid input\n")

        # If user guesses right, set the flag to false and print a message
        elif int(player_guess) == to_guess:
            print("\nCongrats! You got it!")
            not_guessed = False

        # Decrement attempts and print a message to guide the user towards the number
        elif int(player_guess) != to_guess:
            attempts -= 1
            if int(player_guess) > to_guess:
                print(f"Too high. You have {attempts} attempt(s) remaining.")
            else:
                print(f"Too low. You have {attempts} attempt(s) remaining.")

    # Number was not guessed if attempts is 0
    if attempts == 0:
        print(
            f"\nThe number was {to_guess}. Better luck next time!")

    play_again = input(
        "\nPlay again? Type 'y' for yes, or any other character to exit.\n")

    # Starting the game again if user inputs 'y'
    if play_again == "y":
        system("clear")
        setup()
    else:
        print("\nThank you for playing. See you again!\n")


def read_art_file():
    '''Prints ASCII art to the terminal.'''

    # Get the directory of the script
    file_directory = path.dirname(__file__)

    # Combine with the file's name
    file_path = path.join(file_directory, "art.txt")

    with open(file_path, "r") as art_file:
        print(art_file.read() + "\n")


setup()
