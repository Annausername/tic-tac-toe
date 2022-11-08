# TIC-TAC-TOE

  Tic-Tac-Toe is a game in which two players (player vs computer) seek in alternate turns to complete a row, a column, or a diagonal with either three o's or three x's drawn in the spaces of a grid of nine squares; noughts and crosses. In this particular game player is an 'x' by default and the computer is 'o'.

![Main](https://github.com/Annausername/tic-tac-toe/blob/main/media/main.png)

The live link can be found here - https://tic-tac-toe-anna.herokuapp.com/

## UX

The app runs in the Heroku terminal and consists of two menus:

- __Main menu__ The landing page and where the user can go to the:
- __Information menu__ Here the user can either get more information on the game (history and rules of the sudoku) or get more information on the app (How to enter a puzzle and get the correct solution).
- __Exit option__

__As a player__

- I want to play a game with clear and easy instructions;
- I want to be able to see my scores;
- I want to be able to play the game again or quit easily.

### Existing Features

## Features

- __Modules__

  Some modules had to be imported in order to add certain functionalities to the application.

[os](https://docs.python.org/3/library/os.html): is used to create a function that clears the terminal. This checks if the operating system is either Windows or Linux and triggers the necessary command to delete everything visible in the terminal screen.
[sys](https://docs.python.org/3/library/sys.html): is used only in the typewriter function to print every character of the string individually.
[time](https://docs.python.org/3/library/time.html?highlight=time#module-time): this is also used in the typewriter function to create a delay between each character and also a delay after the function prints the whole message.

![modules](https://github.com/Annausername/tic-tac-toe/blob/main/media/modules.png)

## Introduction

  Once the program runs, the first feature to appear is an ACSII logo:

![ASCII](https://github.com/Annausername/tic-tac-toe/blob/main/media/ASCII.png)

  The user is welcomed to the game and they are asked them to insert their name. The "welcome to the game" statement has a sys.stdout.flush() method applied for a better visual effect. A user is given 3 options of starting the game, heading over to read the rules and quitting the app.
  
## Rules

  Rules section appears with cleaning the terminal window, rules, and 3 options of starting the game, heading over back to the main menu and quitting the app.
  
![Rules](https://github.com/Annausername/tic-tac-toe/blob/main/media/Rules.png)  
  
