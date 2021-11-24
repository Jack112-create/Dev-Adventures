import time
from functions import clear_terminal, game_over
from player import Player
from rooms import Room
from questions import (
    html_questions, css_questions,
    javascript_questions, python_questions
)


class Game:
    """
    Game instance brings player through each room,
    giving the player choices to make.
    """