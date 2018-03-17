"""Helper functions for hangman script."""
from random import randrange
from player import Player
from display import MSG


with open('english_dictionary.txt') as english_dictionary:
    DICTIONARY = set(word.strip() for word in english_dictionary)


def choose_players():
    """Prompt user input for num of players (1/2) and player names. Return 2 Player objects.

       Computer Player object automatically chosen for 2nd player in 1 player game.
    """
    no_of_players = None
    while no_of_players not in ('1', '2'):
        no_of_players = input(MSG['players']).strip()

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
        name = input(MSG['name_choice'] % player).strip().capitalize()
        if not name.isalnum():
            print(MSG['err_alnum'])
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
            word = input(MSG['word_choice'] % player.name).strip().lower()
            if word not in DICTIONARY:
                print(MSG['err_dict_word'])
                word = None
    return word


def prompt_for_guess(game):
    """Prompt player for guess. Validate player guess. Return str."""
    valid_guess = None
    while not valid_guess:
        guess = input(MSG['guess'] % game.player.name).strip()
        valid_guess, err_msg = game.validate_player_guess(guess)
        if err_msg: print(err_msg)
    return guess


def clear_screen():
    """Print 30 new lines to screen."""
    print('\n' * 30)


def play_again():
    """Prompt user input to play again. Return boolean."""
    choice = None
    while choice not in ('Y', 'YES', 'N', 'NO'):
        choice = input(MSG['play_again']).upper().strip()
    return CHOICE_DICT[choice]


CHOICE_DICT = {
    'Y': True,
    'YES': True,
    'N': False,
    'NO': False
}
