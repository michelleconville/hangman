"""
Used for libraries and imports
"""
import random  # Randomly selects a word for the game
import os  # Used to clear screen
import colorama  # Adds color to game text
from colorama import Fore, Style
from lives import lives_left  # Hangman lives visual from lives.py

colorama.init(autoreset=True)


def game_intro():
    '''
    Game welcome and request users name and prints Hello name
    '''
    print(
        """
        ██      ███████ ████████ ███████     ██████  ██       █████  ██    ██
        ██      ██         ██    ██          ██   ██ ██      ██   ██  ██  ██
        ██      █████      ██    ███████     ██████  ██      ███████   ████
        ██      ██         ██         ██     ██      ██      ██   ██    ██
        ███████ ███████    ██    ███████     ██      ███████ ██   ██    ██

        ██   ██  █████  ███    ██  ██████  ███    ███  █████  ███    ██
        ██   ██ ██   ██ ████   ██ ██       ████  ████ ██   ██ ████   ██
        ███████ ███████ ██ ██  ██ ██   ███ ██ ████ ██ ███████ ██ ██  ██
        ██   ██ ██   ██ ██  ██ ██ ██    ██ ██  ██  ██ ██   ██ ██  ██ ██
        ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████
        """
    )
    print("Welcome")
    name = " "
    while True:
        name = input("Please enter your name: \n")

        if name.isalpha() is not True:
            print("Error: Your name must be alphabetic only.\n")
        else:
            print("\n")
            print(f'{Fore.YELLOW+Style.BRIGHT}Hello {name}!')
            return name


def start_game():
    '''
    Starts the game with options:
    1 to play - default level easy
    2 to select level of play
    3 to see the game rules
    '''
    print("\n")
    print("Press 1 to Start playing game")
    print("Press 2 to Choose the level to play at")
    print("Press 3 to Read the rules")
    options = False
    while not options:
        settings = input("\n ")
        if settings == "1":
            options = True
            difficulty = "default"
            return difficulty

        elif settings == "2":
            options = True

        elif settings == "3":
            options = True
            game_rules()

        else:
            print(" Please select 1, 2 or 3 to make your choice")


def select_game_level():
    """
    Function to select level
    """
    print("Please select a level\n")
    print("Press e for Easy")
    print("Press n for Normal")
    print("Press h for Hard")
    difficulty = False
    while not difficulty:
        options = input("\n ").lower()
        if options == "e":
            difficulty = True
            num_lives = 10
            return num_lives

        elif options == "n":
            difficulty = True
            num_lives = 7
            return num_lives

        elif options == "h":
            difficulty = True
            num_lives = 5
            return num_lives
        else:
            print("\n Please choose E, N or H to select your level")


def get_random_word():
    """
    Picks a random word from words.txt
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.lower()


def game_rules():
    """
    Explains to the User how to play the game
    """
    print(f'{Fore.CYAN+Style.BRIGHT}Welcome to World Countires Hangman rules \n')
    print("This is a guess the word game")
    print("Guess the word by inputting letters")
    print("If you guess the wrong letter you loose a life")
    print("Your Hang-Hangman will then start to build")
    print("When you reach 0 lives your will be HANGED! \n")
    print(f'{Fore.MAGENTA+Style.BRIGHT}Good luck \n')
    print("Press enter to return to the main menu")


def hangman_lives(lives):
    """
    Displays Hangman visuals
    """
    for _ in lives_left:
        return lives_left[lives]


def play_game(word, num_lives):
    """
    Runs the game and starts all the gameplay logic.
    """
    word_to_guess = '﹍' * len(word)
    game_over = False
    guesses = []
    lives = num_lives
    print(f'\nLives: {lives}\n')
    print('What country are you looking for? '+' '.join(word_to_guess) + '\n')

    while not game_over and lives > 0:
        user_guess = input('Please guess a letter: \n').lower()
        try:
            if len(user_guess) > 1:
                raise ValueError(
                    f"\nYou can't guess more than one letter at a time."
                    f'You guessed: {len(user_guess)}'
                )

            elif not user_guess.isalpha():
                raise ValueError(
                    f'\nYou can only guess by letters.'
                    f'You guessed: {(user_guess)}'
                )

            elif len(user_guess) == 1 and user_guess.isalpha():
                if user_guess in guesses:
                    raise ValueError(
                        f'\n{(user_guess)} has already been used.'
                    )

            elif user_guess not in word:
                print(f'Sorry.. {user_guess} is not a part of the word.')
                print('Better luck next time, you lost a life..')
                guesses.append(user_guess)
                lives -= 1
            else:
                print(f'\n{user_guess} is a part of the word, great job!')
                guesses.append(user_guess)
                guessed_words_list = list(word_to_guess)
                indices = [i for i, letter in enumerate(word)
                           if letter == user_guess]
                for index in indices:
                    guessed_words_list[index] = user_guess
                    word_to_guess = ''.join(guessed_words_list)
                if '﹍' not in word_to_guess:
                    game_over = True

        except ValueError as input_error:
            print(f'{input_error}\n Please try again.\n')
            continue

    print(hangman_lives(lives))

    if lives > 0:
        print(f'\nRemaining tries: {lives}')
        print('What country are we looking for?'
              '+' '.join(word_to_guess) + ')
        print('Your guesses: '+', '.join(guesses) + '\n')

    if game_over:
        print(f'Well done! You guessed the word: {word}')
    else:
        print('You have no lives left.')
        print('Game over.\n')
        print(f'The word you were looking for was: {word}')

    restart_game()


def game_over():
    """
    Graphic for game over display
    """
    print(Fore.RED+Style.BRIGHT +
        """
         ██████   █████  ███    ███ ███████
        ██       ██   ██ ████  ████ ██
        ██   ███ ███████ ██ ████ ██ █████
        ██    ██ ██   ██ ██  ██  ██ ██
         ██████  ██   ██ ██      ██ ███████

         ██████  ██    ██ ███████ ██████
        ██    ██ ██    ██ ██      ██   ██
        ██    ██ ██    ██ █████   ██████
        ██    ██  ██  ██  ██      ██   ██
         ██████    ████   ███████ ██   ██
        """
    )

def win_game():
    """
    Graphic for win game display
    """
    print(Fore.GREEN+Style.BRIGHT +
        """
        ██    ██  ██████  ██    ██
         ██  ██  ██    ██ ██    ██
          ████   ██    ██ ██    ██
           ██    ██    ██ ██    ██
           ██     ██████   ██████

        ██     ██ ██ ███    ██
        ██     ██ ██ ████   ██
        ██  █  ██ ██ ██ ██  ██
        ██ ███ ██ ██ ██  ██ ██
         ███ ███  ██ ██   ████
        """
    )


def restart_game():
    """
    Gives User the choice to Restart the Game or Return to main screen
    """
    game_restart = False

    while not game_restart:
        restart = input(f"{Fore.GREEN+Style.BRIGHT}"
                        f"Would You Like To Play Again :) ? "
                        f"Please Type y for Yes & n for No: ").lower()
        try:
            if restart == "y":
                game_restart = True
                start_game()
            elif restart == "n":
                game_restart = True
                print("\n")
                main()
            else:
                raise ValueError(f"{Fore.RED+Style.BRIGHT}"
                                 f"Please type either y or n,"
                                 f"to make your Choice.You typed{(restart)}")

        except ValueError as e_values:
            print(f"{e_values}.\n{Fore.RED+Style.BRIGHT}"
                  f"Please try again\n")


def clear_screen():
    """
    Used to clear Terminal screen
    """
    os.system("clear")


def main():
    """
    Runs functions used for the Game
    """
    game_intro()
    level = start_game()
    if level == "default":
        num_lives = 10
    else:
        num_lives = select_game_level()
    word = get_random_word()
    play_game(word, num_lives)
   
main()
