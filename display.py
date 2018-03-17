"""Collection of constants and function to display game progress to terminal."""


def display_board(player, opponent, word, misses):
    """Display game progress to terminal: Board_image, word, misses and players points."""
    print(f"{BOARD_IMAGES[len(misses)]}")
    print(f"{YELLOW}Word: {' '.join(word)}\n{END}")
    print(f"{YELLOW}Misses: {', '.join(misses)}\n{END}")
    print(f"{YELLOW}Points: {player.name} = {player.points}, {opponent.name} = {opponent.points}\n{END}")


# Game Colours
YELLOW = '\033[92m'
BLUE = '\033[94m'
ORANGE = '\033[93m'
RED = '\033[91m'
END = '\033[0m'


# The 10 stages of the game
BOARD_IMAGES = {
    0: f'''{YELLOW}
            
              
            
              
        
        ______________


        {END}''',
    1: f'''{YELLOW}
            ______
            |    
            |   
            |    
            | 
        ____|_________


        {END}''',
    2: f'''{YELLOW}
            ______
            |    
            |   
            |    
            | _______
        ____|/_______\_


        {END}''',
    3: f'''{YELLOW}
            ______
            |    
            |   
            |    
            | __/____
        ____|/_______\_


        {END}''',
    4: f'''{YELLOW}
            ______
            |    
            |   
            |    
            | __/_\__
        ____|/_______\_


        {END}''',    
    5: f'''{YELLOW}
            ______
            |    
            |   
            |    |
            | __/_\__
        ____|/_______\_


        {END}''',
    6: f'''{YELLOW}
            ______
            |    
            |   _
            |    |
            | __/_\__
        ____|/_______\_


        {END}''',    
    7: f'''{ORANGE}
            ______
            |    
            |   _ _
            |    |
            | __/_\__
        ____|/_______\_


        {END}''',
    8: f'''{ORANGE}
            ______
            |    
            |   _O_
            |    |
            | __/_\__
        ____|/_______\_


        {END}''',
    9: f'''{RED}
            ______
            |    |
            |   _0_
            |    |
            |   / \  
        ____|__________


        {END}'''
}


# Dict of screen msg output
MSG = {
    'welcome': f'\n{YELLOW}Welcome to Hangman....\nPress Ctrl-C to exit at any time....\n{END}',
    'goodbye': f'\n{YELLOW}Thanks for playing! See you again soon!\n{END}',
    'players': f'{YELLOW}Num of players 1/2?\n-->{END} ',
    'name_choice': f'{YELLOW}%s please input your name\n-->{END} ',
    'word_choice': f'{YELLOW}Please choose a secret word %s...\n-->{END} ',
    'guess': f'{YELLOW}Guess a letter or the word %s!\n-->{END} ',
    'play_again': f'{YELLOW}Play Again? (Y)es/(N)o?\n-->{END} ',
    'winner': f'{BLUE}   %s wins!!!\n{END}',
    'err_alnum': f'{RED}Name needs to be alphanumeric!{END}',
    'err_dict_word': f'{RED}Word needs to be a dictionary word. No cheating!!!{END}',
    'err_alpha': f'{RED}Must be alphabetical characters!{END}',
    'err_guess_len': f'{RED}Guess a single letter or the entire word!{END}',
    'err_prev_guess': f'{RED}Already tried that one, guess again!{END}'
}
