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

    # Checks to see if the player has lost all of their confidence and ends game if true.
    def is_player_dead(self):
        if self.user.confidence <= 0:
            game_over()

    def morning(self):
        clear_terminal()
        time.sleep(1)
        print("It's really early in the morning and your alarm goes off.")
        print("Will you?:\n")
        print('1 Go back to sleep.')
        print('2 Get up and get dressed.')

     # Validating user input. Catching any unexpected input.
        morning_choice = ''
        while morning_choice not in [1, 2]:
            try:
                morning_choice = int(input('> '))
                if morning_choice == 1:
                    clear_terminal()
                    print('\nYou really gave up on your journey that easy?\n')
                    self.user.lower_confidence(self.user.confidence)
                    self.is_player_dead()
                    break
                elif morning_choice == 2:
                    self.kitchen()
                    break
                else:
                    print("\nInvalid choice. Please type either 1 or 2.")
                    continue
            except ValueError:
                print("\nYou cannot input any text. You must type either 1 or 2.")
                continue

    def kitchen(self):
        print("\nYou put your clothes on and make you're way into the kitchen.")
        print("Friends is on the TV.")
        print("Will you?:\n")
        print("1 Eat breakfast and drink some coffee.")
        print("2 Watch 5 seasons of Friends. ")