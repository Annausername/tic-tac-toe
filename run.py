import time  # time delay for game intro
import os # for the underlying os interaction
import sys # for built-in modules

def message(text):
    """
    Prints out a message with a time delay.
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.1)
    time.sleep(1)

message("Welcome to the classic Tic-Tac-Toe game (also called Noughts and Crosses) ^‿◕\n")

def player_name():
    """
    Gets a player name and prints out a welcome message.
    """
    while True:
        name = input("\nWhat is your name, stranger?: \n").capitalize()
        print(f"\nLet's roll, {name}!")
        break
player_name()

def main_menu():
    """
    Gives a player 3 options of running the game,
    reading the rules or exiting the app.
    """
    while True:
        print('\nEnter start to play Tic-Tac-Toe;')
        print('help to read game rules;')
        print('or quit if you want to leave :(')
        choice = input("\nWhat is the next stop?: ")
        if choice in ["Quit", "quit", "Q", "q"]:
            quit_app()
        elif choice in ["Help", "help", "H", "h"]:
            rules()
        elif choice in ["Start", "start", "S", "s"]:
            start_game()
        else:
            wrong_input(choice)



main_menu()