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

        # Validating user input. Catching any unexpected input.
        kitchen_choice = ''
        while kitchen_choice == '':
            try:
                kitchen_choice = int(input('> '))
                if kitchen_choice not in [1, 2]:
                    print("\nPlease type 1 or 2.")
                    kitchen_choice = ''
                    continue
                else:
                    if kitchen_choice == 1:
                        self.drink_coffee()
                        break
                    elif kitchen_choice == 2:
                        clear_terminal()
                        print("You end up watching Friends all day and forget about your coding.")
                        self.user.lower_confidence(self.user.confidence)
                        self.is_player_dead()
                        break
            except ValueError:
                print("\nYou cannot enter any text. You must type either 1 or 2.")
                continue

    def drink_coffee(self):
        clear_terminal()
        print('You eat your breakfast and drink your coffee.')
        time.sleep(1)
        print("You're now feeling AWAKE and ready to start learning how to code.\n")
        time.sleep(1)
        self.choose_room(self.rooms)

    def choose_room(self, rooms):
        """
        Prints each room and its index value,
        asks user to select the room to play.
        """

        while len(rooms) > 0:
            print("Which language would you like to learn?:")
            for index, value in enumerate(rooms):
                print(index + 1, value)
            try:
                choice = int(input('> '))
                room = self.rooms[choice - 1]
                if room == 'HTML':
                    self.play_quiz(self.html_room)
                    continue
                elif room == 'CSS':
                    self.play_quiz(self.css_room)
                    continue
                elif room == 'JavaScript':
                    self.play_quiz(self.javascript_room)
                    continue
                elif room == 'Python':
                    self.play_quiz(self.python_room)
                    continue
            except ValueError:
                print(f"""
Invalid choice. You must type a number from 1 - {len(rooms)}.
""")
                continue
            except IndexError:
                print(f"""
You must type a number from 1 - {len(rooms)}.
""")
                continue