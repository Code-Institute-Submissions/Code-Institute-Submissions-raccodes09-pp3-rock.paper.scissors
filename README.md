# Rock, Paper, Scissors

[Live webpage](https://pp3-rps-ad0039afcece.herokuapp.com/)

![Mockup image](/assets/images/welcome.png)

## Project Overview

Rock, Paper, Scissors is a classic game  that challenges users against the computer in winning through their selections. 

They are asked to enter their username and followed by their first choice. The game will continue to ask the player their choices until the either the player or the computer reaches 3 wins. At which point, the program will ask the user if they want to play again.


### User Experience

#### Design

At this time, the design of the app was based on the template provided by Code Institute. No unique design/animation added at this stage as ensuring the basic were working i.e. the game ran as it should.

## Flowchart

Using Lucidchart I was able to design my game before building it. It allowed me to draw up an basic layout and flow that I wanted to include.

![Mockup image](/assets/images/flowchard.png)


## Features

- Username entry.
- "One-page" website.
- Prompt to choose first selection
- Prompts to continue choosing selections until first player to score three wins
- Once the score has reached three, message will appear advising the winner
- User will be asked if they want to play again.

#### Welcome 

![Mockup image](/assets/images/welcome.png)

#### First Selection

![Mockup image](/assets/images/first.selection.png)

#### Result Page

![Mockup image](/assets/images/endgame.png)

## Technologies Used

### Languages

- HTML (Template)

- JavaScript (Template)

- Python

### Frameworks, Libraries & Other Resources

1. [Python Tutor:](https://pythontutor.com/)
    - Used to step through code to resolve issues.

1. [Heroku:](https://heroku.com/)
    - Heroku was used for the deployed application.

1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

1. [GitHub:](https://github.com/)
    - GitHub used to store the code whoch was pushed from Git.

1. [Lucid:](https://www.lucidchart.com/pages/)
    - Lucidchart was used to design the wireframes



## Validator Testing

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check Python code.

    - [PYTHON](/assets/testing/validation-pdf/html-validation.pdf)

#### No Validation testing was carried out on HTML / JavaScript as no changes made to template


## User Testing

- Feedback from user testing was mostly postive based on their expectations.
- Reviews suggested that:
    - the app was easy to navigate
    - the basic layout and structure of the prompts made the intention clear
    - include more appealing visual appearance
    - Add images to support the games intention
    - imporve readability of text

- The webiste worked efficently and without issue across laptop, tablet and mobile phone devices.


## Bugs

- Initially the score counter after each round wasn't adding up causing the game to go into a continuous loop. I resolved this by moving the score check inside the game loop.

## Future Implementations

- Scoreboard where previous users and their scores are saved which would add further competitivness to the game.
  
- Allow for player versus player selection.

- Animations for when the player selects their choices
  
- Add animation for when user logs in and also when their final result is revealed.

## Deployment

### Heroku

The project was deployed to Heroku using the following steps:

1. Log in to GitHub and locate [Rock, Paper, Scissors](https://github.com/raccodes09/pp3-rock.paper.scissors).
1. Fork or clone this repository.
1. Create a new Heroku app.
1. Set the buildbacks to python and NodeJS in that order.
1. Link the Heroku app to the respository.
1. Click on Deploy.


## Credits

### Content

- Code from social media links was taken from CI Love Running project.

- [Youtube](https://www.youtube.com/) Further learing and understanding of Python.

- [W3Schools](https://www.w3schools.com/) Information on loop structures.

- [Stack Overflow](https://stackoverflow.com/) Assisted with score counter.

- Deployment section of README.md provided by a combination of CI's template and generic template on slack.

### Media

No media was used at this stage

## Acknowledgements

The Slack community for asking questions that I didn't know I needed to ask and providing valuable help throughout.

Tutors and Student support from Code Institute - very helpful and understanding throughout the course.
