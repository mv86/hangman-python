"""Helper functions for hangman script."""
from random import randrange
from player import Player
from game_colours import YELLOW, RED, END


with open('english_dictionary.txt') as english_dictionary:
    DICTIONARY = set(word.strip() for word in english_dictionary)


def choose_players():
    """Prompt user input for num of players (1/2) and player names. Return 2 Player objects.

       Computer Player object automatically chosen for 2nd player in 1 player game.
    """
    no_of_players = None
    while no_of_players not in ('1', '2'):
        no_of_players = input(f'{YELLOW}Num of players 1/2?\n-->{END} ').strip()

    player_name = _choose_name('Player 1')
    player1 = Player(player_name)

    if no_of_players == '2':
        player_name = _choose_name('Player 2')
        player2 = Player(player_name)
        return player1, player2

    return player1, Player('Computer')


def _choose_name(player):
    """Helper function for choose_players."""
    name = None
    while not name:
        name = input(f'{YELLOW}{player} please input your name\n-->{END} ').strip().capitalize()
        if not name.isalnum():
            print(f'{RED}Name needs to be alphanumeric!{END}')
            name = None
    return name


def choose_word(player):
    """Prompt player2 for word choice. Return str"""
    if player.name == 'Computer':
        rand_idx = randrange(len(DICTIONARY))
        word = list(DICTIONARY)[rand_idx]
    else:
        word = None
        while not word:
            word = input(f'{YELLOW}Please choose a secret word {player.name}...\n-->{END} ').strip().lower()
            if word not in DICTIONARY:
                print(f'{RED}Word needs to be a dictionary word. No cheating!!!{END}')
                word = None
    return word


def validate_player_guess(game):
    """Prompt player for guess. Validate player guess. Return str."""
    guess = None
    while not guess:
        guess = input(f'{YELLOW}Guess a letter or the word {game.player.name}!\n-->{END} ')
        if not guess.isalpha():
            print(f'{RED}Must be alphabetical characters!{END}')
            guess = ''
        if len(guess) > 1 and len(guess) < len(game.opponent.word):
            print(f'{RED}Guess a single letter or the entire word!{END}')
            guess = ''
        if guess.upper() in game.word or guess.lower() in game.misses:
            print(f'{RED}Already tried that one, guess again!{END}')
            guess = ''
    return guess


def play_again():
    """Prompt user input to play again. Return boolean."""
    choice = None
    while choice not in ('Y', 'YES', 'N', 'NO'):
        choice = input(f'{YELLOW}Play Again? (Y)es/(N)o?\n-->{END} ').upper().strip()
    return CHOICE_DICT[choice]


CHOICE_DICT = {
    'Y': True,
    'YES': True,
    'N': False,
    'NO': False
}
