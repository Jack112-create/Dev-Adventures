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

    def show_stats(self):
        print(f"""
{self.name.upper()} THE DEVELOPER!
Here are your stats:
Name: {self.name}
----------------------
Confidence: {self.confidence}
----------------------
Skills: {self.skills}
----------------------
Job: {self.job}
----------------------
Score: {self.score}
""")