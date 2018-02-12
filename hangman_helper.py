"""Helper functions for hangman script."""
from player import Player


def choose_players():
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
    name = None
    while not name:
        name = input(f'\n{player} please input your name\n--> ').capitalize().strip()
        if not name.isalnum():
            print('\nError! Name needs to be alphanumeric!\n')
            name = None
    return name


def play_again():
    choice = None
    while choice not in ('Y', 'YES', 'N', 'NO'):
        choice = input('\nPlay Again? (Y)es/(N)o?\n--> ').upper().strip()
        print(choice)
    return CHOICE_DICT[choice]


CHOICE_DICT = {
    'Y': True,
    'YES': True,
    'N': False,
    'NO': False
}
