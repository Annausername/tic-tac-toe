import time  # time delay for game intro
import os  # for the underlying os interaction
import sys  # for built-in modules

print("\n")
print(" __ __|_ _|  ___|        __ __|  \     ___|        __ __| _ \  ____|")
print("    |    |  |               |   _ \   |               |  |   | __|  ")
print("    |    |  |     _____|    |  ___ \  |     _____|    |  |   | |    ")
print("   _|  ___|\____|          _|_/    _\\____|          _| \___/ _____|")
print("\n")


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
        choice = input("\nWhat is the next stop?: \n")
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
    Gives options to either starting the game,
    exiting the app or going back to the main menu.
    """
    cls()
    time.sleep(0.5)
    print("The game is played on a grid that's 3 squares by 3 squares.\n")
    print("You are 'x', the computer is 'o'.\n")
    print("You are the one to hit first by choosing the cell number.\n")
    print("Your hit should be a number between 1 and 9.\n")
    print("_1_|_2_|_3_")
    print("_4_|_5_|_6_")
    print(" 7 | 8 | 9 ")
    print("\nThe first player to get 3 of the marks in a row")
    print("(up, down, across, or diagonally) is the winner.\n")
    print("When all 9 squares are full, the game is over.\n")
    time.sleep(1)
    while True:
        print('Shall we proceed?\n')
        print('Enter start to play the game;')
        print('home to return to the main menu;')
        print('or quit if you want to exit the app!')
        choice = input("\nPlese select an option: \n")
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


def wrong_input(choice):
    """
    Message for incorrect input values.
    """
    print('Please enter the required option.')


def quit_app():
    """
    Exits the app with a confirmation question.
    """
    print("\nDo you really want to quit?")
    while True:
        choice = input("yes/no: \n")
        if choice in ["yes", "Yes", "y", "Y"]:
            message("\nSorry you are leaving. Come back to play again!\n")
            quit()
        elif choice in ["no", "No", "N", "n"]:
            break
        else:
            wrong_input(choice)


def draw_board():
    """
    Prints out the game board pannel.
    """
    print("\nLife if full of choices. Make the right one.\n")
    print(board[1] + ' | ' + board[2] + '| ' + board[3])
    print('--+--+--')
    print(board[4] + ' | ' + board[5] + '| ' + board[6])
    print('--+--+--')
    print(board[7] + ' | ' + board[8] + '| ' + board[9])
    print('\n')


def player_move(hit):
    """
    Gives a player an option to make the move.
    """
    while True:
        try:
            move = int(input('Hit the spot between 1 and 9: \n'))
            if move in range(1, 10):
                if board[move] == ' ':
                    return move
                else:
                    print("Aww.. This cell is occupied.")
            else:
                print('No cheating! Hit again from 1 to 9: \n')
        except ValueError:
            print("Only numbers accepted. Hit again: \n")


def is_winning(hit, board):
    """
    Checks all the possible variants for the win of all players.
    """
    win_option = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for option in win_option:
        if board[option[0]] == board[option[1]] == board[option[2]] == hit:
            return True


def win_hit(cell, board, computer):
    """
    Creates a temporary board and inserts a computer move
    to check if it is a win one.
    """
    copy_board = list(board)
    copy_board[cell] = computer
    if is_winning(computer, copy_board):
        return True
    else:
        return False


def computer_move(computer, player, board):
    """
    Makes a computer move taking into consideration the win move.
    """
    for cell in range(1, 10):
        if board[cell] == ' ' and win_hit(cell, board, computer):
            return cell
    for cell in range(1, 10):
        if board[cell] == ' ' and win_hit(cell, board, player):
            return cell
    for cell in [5, 1, 7, 3, 2, 9, 8, 6, 4]:
        if board[cell] == ' ':
            return cell


def restart_game():
    """
    Gives an option for restarting the game or quitting an app.
    """
    while True:
        choice = input('Do you want to play again?:\n')
        if choice in ['yes', 'Yes', 'y', 'Y']:
            print("\nLet's play another round!")
            start_game()
        elif choice in ['no', 'No', 'n', 'N']:
            quit_app()
        else:
            wrong_input(choice)
    else:
        return False


def who_won(player, computer):
    """
    Checks if either player or won
    """
    win_option = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
    for option in win_option:
        if board[option[0]] == board[option[1]] == board[option[2]] == player:
            print('Congratulations! You won this one!')
            if not restart_game():
                return False
        elif board[option[0]] == board[option[1]] == board[option[2]] == computer:
            print('Computer won this game. Better Luck next time!')
            if not restart_game():
                return False
    if ' ' not in board:
        print("It's a draw!")
        if not restart_game():
            return False
    return True


def start_game():
    """
    Initiates the actual game.
    """
    cls()
    global board
    play = True
    board = ["",
             " ", " ", " ",
             " ", " ", " ",
             " ", " ", " "]
    player = 'x'
    computer = 'o'
    draw_board()
    while play:
        x = player_move(player)
        board[x] = player
        draw_board()
        play = who_won(player, computer)
        o = computer_move(computer, player, board)
        print(f'Computer hits: {o}')
        board[o] = computer
        draw_board()
        play = who_won(player, computer)


main_menu()
