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

def game_rules():
    """
    Explains to the User how to play the game
    """
    print("Welcome to World Countires Hangman rules")
    print("This is a guess the word game")
    print("Guess the word by inputting letters")
    print("If you guess the wrong letter you loose a life")
    print("Your Hang-Hangman will then start to build")
    print("When you reach 0 lives your will be HANGED!")
    print("Good luck")
    print("Press enter to return to the main menu")

def main():
    """
    Runs functions used for the Game
    """
    
    game_rules()

main()