from adventure.game import Game
from adventure.functions import clear_terminal, game_over
import time


def title_screen():
    time.sleep(1)
    print("""
    #############################
    + Welcome to Dev Adventure! +
    ############################""")
    time.sleep(1)
    print("""
    .__________________________.
    | .___________________. |==|
    | | ................. | |  |
    | | [ Hello World! ]  | |  |
    | | ::::::::::::::::: | | ,|
    | !___________________! |(c|
    !_______________________!__!
   \                            /
  \  [][][][][][][][][][][][][]  /
 \  [][][][][][][][][][][][][][]  /
(  [][][][][____________][][][][]  )
 \ ------------------------------ /
  \______________________________/""")
    time.sleep(1)
    print("""
    -          Play           -
    -          Rules          -
    -          Quit           -
    Type 'play', 'rules' or 'quit'.""")
    title_screen_selections()


def rules_menu():
    clear_terminal()
    print('###########################')
    print('+       How To Play       +')
    print('###########################')
    print('- Do not let your confidence drop to 0.')
    print('- Get all the skills you need to become a Junior Developer.')
    print('- Good luck and have fun!')
    print('\nType "play" or "quit"')
    title_screen_selections()


def title_screen_selections():
    # Validating users input to ensure they select one of the screens.
    screen_choice = ''
    while screen_choice not in ['play', 'rules', 'quit']:
        screen_choice = input('> ').lower()
        if screen_choice == 'play':
            intro_scene()
            break
        elif screen_choice == 'rules':
            rules_menu()
            break
        elif screen_choice == 'quit':
            game_over()
            break
        else:
            print('\nInvalid choice. Please type "play", "rules" or "quit".')
            continue


def intro_scene():
    clear_terminal()
    print("""
Hello there adventurer! It's time to embark on your journey of becoming a Full
Stack Developer.
This won't be the easy journey as it requires a lot of patience and self belief.
You will face a series of challenges throughout your journey that will mould
you into becoming a great developer!

Before we begin this new and exciting journey you must enter your name:""")

    user = input('> ').capitalize().strip()
    # Validating users input to ensure it's not left empty.
    while True:
        if len(user) <= 0:
            print('Please enter your name:')
            user = input('> ').capitalize()
            continue
        else:
            game = Game(user)
            game.start()
            break
