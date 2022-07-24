# chess-ai

A deep learning chess ai

stores possible moves for each game situation in a json file with win loss values and adjusts them in the learning/training process.

Current state of this project:
-> Unit Tests need to be added for the most important functions (Move calculations done soon, learning process tests outstanding)
-> I'd like to code my own chess GUI for this project, however if you prefer integrating this AI into an existing GUI than you can of course do so yourself
-> Some code clean up is needed imo
-> Performance improvements outstanding

Important Notes:
The unit tests use and delete the logfile and database!
Do not run them on a directory where you want to store a trained AI database!
To run many tests in a row, add a loop to the main file (it's not in there because I don't want you to accidently flood your hard drive with tons of GB of data when running the code the first time)

Prerequisites:

1. Install Python on your machine first!
2. Install Django: python3 -m pip install Django
   or: python -m pip install Django

Commands:

- Run unit tests: python3 -m unittest discover -s test

- Run webserver for the progress overview: python3 manage.py runserver
  (This requires to run the chess AI a few times to have data to work with, else the index page will not show data! )

- Run the AI without server locally: python3 main.py
