import time  # time delay for game intro
import os # for the underlying os interaction
import sys # for built-in modules

print("Welcome to the classic Tic-Tac-Toe game (also called Noughts and Crosses) ^‿◕\n")
def player_name():
    """
    Gets a player name and prints out a welcome message.
    """
    while True:
        name = input("\nWhat is your name, stranger?: \n").capitalize()
        print(f"\nLet's roll, {name}!")
        break
