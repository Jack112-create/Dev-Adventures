import time
from adventure.functions import clear_terminal, game_over
from adventure.player import Player
from adventure.rooms import Room
from adventure.questions import (
    html_questions, css_questions,
    javascript_questions, python_questions
)


class Game:
    """
    Game instance brings player through each room,
    giving the player choices to make.
    """

    def __init__(self, user):
        self.user = Player(user)
        self.rooms = ['HTML', 'CSS', 'JavaScript', 'Python']
        self.html_room = Room('HTML', html_questions)
        self.css_room = Room('CSS', css_questions)
        self.javascript_room = Room('JavaScript', javascript_questions)
        self.python_room = Room('Python', python_questions)
    
    def start(self):
        clear_terminal()
        self.user.show_stats()
        print('Type "c" to continue or "q" to quit.')

        # Validating user input.
        answer = ''
        while answer not in ['c', 'q']:
            answer = input('> ').lower()
            if answer == 'c':
                self.morning()
            elif answer == 'q':
                game_over()
            else:
                print('\nInvalid choice. Please type "c" or "q".')