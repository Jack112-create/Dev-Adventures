# Dev Adventures!

## Introduction
Dev Adventures is a text-based adventure game where the user takes on the journey of becoming a Full Stack Developer by answering tech questions and collecting new skills as they progress.
The game is built using python and is played by entering commands into the terminal that is provided to the user.

## Table of Contents

* [User Experience](#Introduction)
    * [Site Goals](#Site-Goals)
    * [User Stories](#User-Stories)
    * [Strategy Plane](#Strategy)
    * [Scope Plane](#Scope)
    * [Structure Plane](#Structure)
    * [Surface Plane](#Surface)
        * [Design](#Design)
    * [Features](#Features)
    * [Testing](#Testing)
    * [Bugs](#Bugs)
    * [Deployment](#Deployment)
    * [Credits](#Credits)
    
## UX

### User Stories
* As a user, when I first visit the game I would like to be given the following choices:
    - Play the game. 
    - View the game rules.
    - Quit the game.
* As a user, I want an interesting storyline.
* As a user, I want to select to be able to select a quiz room.
* As a user, I want a challenging game that has repercussions if I do not make the correct choice.
* As a user, I want a message to be displayed to notify me if I have gotten a question correct or incorrect.
* As a user, I want to be able to view my stats throughout the game.
* As a user, I want a score system that is tracked as I progress through each challenge.

### Site Goals
* Create a simple fun to play text based adventure.
* Provide users with an interesting story.
* Provide users with difficult questions throughout the game.
* Provide the user with pop up challenge that requires an answer within the given time limit.

### Strategy
Dev Adventures is intended to be a fun to play text based adventure that provides the user with an exciting
storyline of becoming a Full Stack Developer. The user must prove that they are worthy of becoming a Full Stack Developer
by completing a series of challenges and obtaining the required skillset to become a Developer.

### Scope
Features to be included:

- Title Screen - The first screen that the user should see when starting the game is the title screen.
The title screen displays the name of the game and gives the user options to play the game, 
view the game rules or to quit the game.

- Quiz - The game should have quiz like rooms that tests the users knowledge of the language that
they have chosen from a list of languages.

- The user should have their own stats that can change throughout the game depending on the actions that they take.

- The user should be provided with a clear indication that the game has completed.

### Structure
- The title Screen provides the user with the options to start the game, view the game rules or to exit the game.

- The introduction scene will ask the user to input their name in order to setup their stats.

- The user will be asked a series of questions as they enter each language room. The changes made to the users stats 
will have either a positive or negative impact depending on if the user has answered the question correctly or not.

- The user is presented with a message that will notify them if they have win/lost the game.

### Surface

#### Design

### Features

#### Title Screen
- The title screen presents the user with the game title and provides options to
play the game, view the game rules or to quit the game

![Title Screen](assets/features/title.png)

**User stories related to this feature:**

* As a user, when I first visit the game I would like to be given the following choices:
    - Play the game. 
    - View the game rules.
    - Quit the game.

#### Rules Screen
- The rules screen provides the user with a brief overview on how to play the game.

**User stories related to this feature:**

* As a user, when I first visit the game I would like to be given the following choices:
    - Play the game. 
    - View the game rules.
    - Quit the game.

![Rules Screen](assets/features/rules.png)

#### Intro Scene
- The intro scene presents the user with the game story and goal. The user must enter their
name in order to create their developer character.

![Intro Scene](assets/features/intro.png)

**User stories related to this feature:**

* As a user, I want an interesting storyline.

#### User Stats
- Once the user has inputted their name, their stats will be printed to the terminal. The users stats
are printed throughout the game so that the user can keep track of their score and confidence level. 

![Stats Screen](assets/features/stats.png)

**User stories related to this feature:**

* As a user, I want to be able to view my stats throughout the game.
* As a user, I want a score system that is tracked as I progress through each challenge.

#### Game Over Screen

- When the user is unsucessful in completing the game, they will be presented with the game over screen.

![Game Over Screen](assets/features/game_over.png)

**User stories related to this feature:**

* As a user, I want a challenging game that has repercussions if I do not make the correct choice.

### Choose Room Screen

- The user is given the option to choose 1 of 4 languages in which they will have to answers questions 
about the language they have chosen.

![Choose Room Screen](assets/features/choose_room.png)

**Site Goal related to this feature:**

* As a user, I want to select to be able to select a quiz room.


#### Correct & Incorrect Message

- As the user plays a quiz room and answers each question correctly or incorrectly, a message is printed
to notify them if they have gotten the question correct or not. If the user answers correctly their score 
will increase. If the user does not answer correctly, their confidence level will decrease.

![Correct Message](assets/features/correct.png)

![Incorrect Message](assets/features/incorrect.png)

**User stories related to this feature:**

* As a user, I want a message to be displayed to notify me if I have gotten a question correct or incorrect.

### Testing


### Bugs

### Deployment

### Credits

#### Media
