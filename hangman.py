#!/home/max/Python/projects/hangman/venv/bin/python
"""Script to start Hangman game."""
from player import Player
from game import Game


def choose_players():
    no_of_players = None
    while no_of_players not in ('1', '2'):
        no_of_players = input('Num of players 1/2?\n--> ')

    p1_name = choose_name('Player 1')
    p1 = Player(p1_name)

    if no_of_players == '2':
        p2_name = choose_name('Player 2')
        p2 = Player(p2_name)
        play_game(p1, p2)

    play_game(p1)


def play_game(p1, p2=Player('Computer')):
    p2.choose_word('hangman') # TODO add functionality
    game = Game(p1, p2)

    # while not game.winner:
    #     p1.guess()
    #     game.check_player_guess()

    # TODO display winner

    if play_again():
        if p2.name != 'Computer':
            game = Game(p2, p1)
        else:
            game = Game(p1, Player('Computer'))

def play_again():
    choice = None
    while choice not in ('Y', 'YES', 'N', 'NO'):
        choice = input('Play Again? (Y)es/(N)o?\n--> ').upper()
        print(choice)
    return CHOICE_DICT[choice]


def choose_name(player):
    name = None
    while not name:
        name = input(f'{player} please input your name\n--> ')
        if not name.isalnum():
            print('\nError! Name needs to be alphanumeric!\n')
            name = None
    return name


CHOICE_DICT = {
    'Y': True,
    'YES': True,
    'N': False,
    'NO': False
}


if __name__ == '__main__':
    choose_players()