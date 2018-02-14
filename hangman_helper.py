"""Helper functions for hangman script."""
from player import Player


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
            print('\nError! Name needs to be alphanumeric!\n')
            name = None
    return name


def word_choice(player):
    """Prompt player2 for word choice."""
    if player.name == 'Computer':
        word = 'hangman' # TODO Add functionality
    else:
        # TODO Add word rules
        word = input(f'\nPlease choose a secret word {player.name}...\n--> ').strip()
    return word


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
