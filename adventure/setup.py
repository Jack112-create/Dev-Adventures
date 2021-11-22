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


def rules_menu():
    clear_terminal()
    print('###########################')
    print('+       How To Play       +')
    print('###########################')
    print('- Do not let your confidence drop to 0.')
    print('- Get all the skills you need to become a Junior Developer.')
    print('- Good luck and have fun!')