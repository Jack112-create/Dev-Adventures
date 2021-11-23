from functions import clear_terminal
import random
import time


class Room:
    """
    Creates an instance of a quiz room,
    passing in the language and questions
    about the language.
    """
    
    def __init__(self, room, room_questions):
        self.room = room
        self.room_questions = room_questions