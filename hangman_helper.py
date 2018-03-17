"""Helper functions for hangman script."""
from random import randrange
from game_objects import Player
from display import MSG


with open('english_dictionary.txt') as english_dictionary:
    DICTIONARY = set(word.strip() for word in english_dictionary)


def start_game():
    """Display welcome message and start game."""
    clear_screen()
    print(MSG['welcome'])
    print('\n' * 3)


def choose_players():
    """Prompt user input for num of players (1/2) and player names. Return 2 Player objects.

       Computer Player object automatically chosen for 2nd player in 1 player game.
    """
    no_of_players = None
    while no_of_players not in ('1', '2'):
        clear_screen()
        no_of_players = input(MSG['players']).strip()

    clear_screen()
    player_name = _choose_name('Player 1')
    player1 = Player(player_name)

    if no_of_players == '2':
        clear_screen()
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
    return name.title()


def choose_word(player2):
    """Prompt player2 for word choice. Return str"""
    if player2.name == 'Computer':
        rand_idx = randrange(len(DICTIONARY))
        word = list(DICTIONARY)[rand_idx]
    else:
        clear_screen()
        word = None
        while not word:
            word = input(MSG['word_choice'] % player2.name).strip().lower()
            if word not in DICTIONARY:
                print(MSG['err_dict_word'])
                word = None
    clear_screen()
    player2.word = word.upper()


def play(game):
    """Perform all actions for one turn of game."""
    game.player.guess = prompt_for_guess(game)
    game.update_game()
    game.check_for_winner()
    clear_screen()
    game.display_game_state()


def prompt_for_guess(game):
    """Prompt player for guess. Validate player guess. Return str."""
    valid_guess = None
    while not valid_guess:
        guess = input(MSG['guess'] % game.player.name).strip()
        valid_guess, err_msg = game.validate_player_guess(guess)
        if err_msg: print(err_msg)
    return guess.upper()


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


def end_game():
    """Display goodbye message and exit game."""
    clear_screen()
    print(MSG['goodbye'])


def clear_screen():
    """Print 50 new lines to screen."""
    print('\n' * 50)
