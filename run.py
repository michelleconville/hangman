import random

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)



def get_random_word():
    """
    Picks a random word from words.txt
    """
    random_word = random.choice(open("words.txt", "r").read().split('\n'))
    return random_word.upper()