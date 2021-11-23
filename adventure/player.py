import random


class Player:
    """
    Creates a player providing a
    level of confidence,
    job, and a list of skills
    """

    def __init__(self, name):
        self.name = name
        self.job = ''
        self.confidence = 100
        self.skills = []
        self.score = 0