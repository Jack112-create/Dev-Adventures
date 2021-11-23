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

    def room_task(self):
        clear_terminal()
        # Instructions on how to play.
        print(f"""
    Welcome to the {self.room} quiz!
    In order to move on with your learning you must put your knowledge of {self.room} to the test!
    You will be asked 5 questions:
    - Get a question right and your score will increase.
    - Get a question wrong and watch both your confidence level and score go down!
    """)

    # End the room.
    def room_over(self):
        clear_terminal()
        print('Congratulations!')
        time.sleep(1)
        print(f'{self.room} has been added to your skills!')
        time.sleep(1)

    def display_question(self, question):
        print(question)
        # Checking if question has been asked and removes it from list.
        for item in self.room_questions:
            if item['question'] == question:
                self.room_questions.pop(self.room_questions.index(item))