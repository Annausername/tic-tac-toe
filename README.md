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



  
### Testing 


- __Bugs__

Solved bugs

 - Footer was not sticky and would always raise to the middle of the page. I had to use a container "wrapper" with a value of min-height to push the footer down.
- Two main images to display as column in a responsive version with a help of css property "display : contents;".
- Community background image doesn't fit the mobile version, so it was removed from the screen size width of 1235px and down. 
- The Community section was not centered on the screen size width from 1000px to 540px, so it was given a property of "width : fit-content".

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
