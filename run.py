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

def rules():
    """
    Prints out game rules for the player.
    Gives options to either starting the game, exiting the app or going back to the main menu.
    """
    cls()
    time.sleep(0.5)
    print("The game is played on a grid that's 3 squares by 3 squares.\n")
    print("You are 'x', the computer is 'o'.\n")
    print("You are the one to hit first by choosing the cell number for your move.\n")
    print("Your hit should be a number between 1 and 9, starting to count horizontally.\n")
    print("_1_|_2_|_3_")
    print("_4_|_5_|_6_")
    print(" 7 | 8 | 9 ")
    print("\nThe first player to get 3 of the marks in a row (up, down, across, or diagonally) is the winner.\n")
    print("When all 9 squares are full, the game is over.\n")
    time.sleep(1)
    while True:
        print('\nShall we proceed?\n')
        print('Enter start to play the game;')
        print('home to return to the main menu;')
        print('or quit if you want to exit the app!')
        choice = input("\nPlese select an option: ")
        if choice in ["Quit", "quit", "Q", "q"]:
            quit_app()
        elif choice in ["Home", "home", "H", "h"]:
            main_menu()
        elif choice in ["Start", "start", "S", "s"]:
            start_game()
        else:
            wrong_input(choice)

def cls():
    """
    Clears the terminal window.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


main_menu()