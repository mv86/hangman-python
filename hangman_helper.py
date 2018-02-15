"""Helper functions for hangman script."""
from random import randrange
from player import Player

# Add colour to error text
ERROR = '\033[91m'
END = '\033[0m'

with open('english_dictionary.txt') as english_dictionary:
    DICTIONARY = set(word.strip() for word in english_dictionary)


def choose_players():
    """Prompt user input for num of players (1/2) and player names. Return 2 Player objects.

       Computer Player object automatically chosen for 2nd player in 1 player game.
    """
    no_of_players = None
    while no_of_players not in ('1', '2'):
        no_of_players = input('\nNum of players 1/2?\n--> ').strip()

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
        name = input(f'\n{player} please input your name\n--> ').strip().capitalize()
        if not name.isalnum():
            print(f'\n{ERROR}Error! Name needs to be alphanumeric!{END}\n')
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
            word = input(f'\nPlease choose a secret word {player.name}...\n--> ').strip().lower()
            if word not in DICTIONARY:
                print(f'\n{ERROR}Error! Word needs to be a dictionary word. No cheating!!!{END}\n')
                word = None
    return word


def validate_player_guess(game):
    """Prompt player for guess. Validate player guess. Return str."""
    guess = None
    while not guess:
        guess = input(f'\nGuess a letter or the word {game.player.name}!\n--> ')
        if len(guess) > 1 and len(guess) < len(game.opponent.word):
            print(f'\n{ERROR}Error! Guess a single letter or the entire word!{END}\n')
            guess = ''
        if guess.upper() in game.word or guess in game.misses:
            print(f'\n{ERROR}Error! Already tried that one, guess again!{END}\n')
            guess = ''
    return guess


def play_again():
    """Prompt user input to play again. Return boolean."""
    choice = None
    while choice not in ('Y', 'YES', 'N', 'NO'):
        choice = input('\nPlay Again? (Y)es/(N)o?\n--> ').upper().strip()
    return CHOICE_DICT[choice]


CHOICE_DICT = {
    'Y': True,
    'YES': True,
    'N': False,
    'NO': False
}
