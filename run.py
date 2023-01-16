import random

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


def game_intro():
    '''
    Game welcome and request users name and prints Hello users name
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

game_intro()

def get_random_word():
    """
    Picks a random word from words.txt
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.upper()