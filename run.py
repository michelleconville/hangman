import random

import colorama
from colorama import Fore, Style

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
            print(f'{Fore.YELLOW+Style.BRIGHT}Hello {name}!')
            return name

def get_random_word():
    """
    Picks a random word from words.txt
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.upper()


def main():
    """
    Runs functions used for the Game
    """
    game_intro()

main()