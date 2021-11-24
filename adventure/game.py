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