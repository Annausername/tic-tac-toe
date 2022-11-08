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
  
## Start Game

  Having clicked start game, a player sees a printed out empty board and an input field to      make a move first (validating the input).
  
![Start game](https://github.com/Annausername/tic-tac-toe/blob/main/media/start.png)  

  After the first move by a player, the new board with the actual hit has been printed out.
The computer's move has been printed out afterwards, and the player has been offered to make another move (validating the input and checks for the occupied cells).

![Move](https://github.com/Annausername/tic-tac-toe/blob/main/media/move.png) 

## End Game

  The game ends when either first player(or computer) get 3s of the marks in a row or all 9 squares are full. The player afterwards is given an option to either restart the game of quit the app.
  
![End Game](https://github.com/Annausername/tic-tac-toe/blob/main/media/end%20game.png)  

## Quit app

  The option of quitting app has a confirmation question to make sure it was not a mistake       enter, and a goodbye message. The last sentence has a sys.stdout.flush() method applied for   a better visual effect. 

![Quit](https://github.com/Annausername/tic-tac-toe/blob/main/media/Exit.png)

*each input has a validation for the correct input type, however, if it is a word it includes capitalization, and the first letter enter (e.g. "Start" -> "Start", "start", "s", "S").
  
### Testing 

  Since pep8online.com is currently down. I've used a PEP8 validator installed to the Gitpod Workspace directly by following these steps:
  
- Run the command pip3 and installed pycodestyle.
- In the workspace, pressed Cmd+Shift+P since in on Mac.
- Entered the "linter" into the search bar that appeared, and clicked on Python: Selected     Linter from the filtered.
- Select pycodestyle from the list.

  PEP3 didn't ahow any errors underlined in red, but I saw the list in the PROBLEMS tab beside the terminal.
  
![Problems](https://github.com/Annausername/tic-tac-toe/blob/main/media/Errors.png)

  In the list above there are 3 problems where the lines are too long, however, this is the part of the code to count the win moves, so I ended up leaving this as it is, and a valid escape sequence for the ASCII logo (never changed it either).

- __Bugs__

Solved bugs

 - The function main_menu() was called right after it was defined, so the game couldn't launch    properly. Fixed this by calling it at the end.
 - Used another algorythm to count the win first breaking them up by functions to check          columns, rows, and diagonals. It took a lot of lines of code and wouldn't works properly,      so I replaced them with one line (which shows up as problem in PIP3 due to the length) to      check all variants at once.

## Deployment

  This project was developed through Gitpod, using the template provided by Code Institute. Every step was documented and pushed thoroughly via GitHub.

The deployment is made using [Heroku](https://www.heroku.com/) following the listed steps:

1. Log in or register a new account on Heroku
2. Click on 'New' in the dashboard and select 'Create New App'
3. Select a name for the app and choose your region.
4. Click on "Create app"
5. When the app is created click on Setting
6. To improve compatibility with various Python libraries add Config Var with Key = PORT and      the Value = 8000
7. Add 2 buildpacks: Python and then Nodejs in this specific order
8. Go back at the top and click on "Deploy" and select "GitHub"
9. Scroll down and click on 'Connect to GitHub'
10. Search for your GitHub repository name by typing it
11. Click on "Connect"
12. Scroll down and click on "Deploy Branch"
13. You will see a message "The app was successfully deployed" when the app is built with         python and all the depencencies
14. Click on view and you will see the [deployed site](https://tic-tac-toe-anna.herokuapp.com/)

## Technologies Used

- [Python](https://www.python.org/);
- [Javascript](https://www.javascript.com/) provided in the Code Institute Template;
- [HTML](https://en.wikipedia.org/wiki/HTML5) provided in the Code Institute Template;
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) provided in the Code Institute     Template.

## Credits

- I've used another student's Tic Tac Toe project as a reference [Link to GitHub](https://github.com/aimansae/p3-tic-tac-toe).
- A few questions were solved during the communication with other students in Slack.
- Browsing through the internet helped find great solutions and fix bugs e.g. [GeeksforGeeks](https://www.geeksforgeeks.org/), [Stack Overflow](https://stackoverflow.com/), [ASCII Generator](https://www.ascii-art-generator.org/) to create an intro image and [PEP8](https://pep8.org/) to make the code look nice a clean.
