#!/home/max/Python/projects/hangman/venv/bin/python
"""Script to start Hangman game."""
from player import Player
from game import Game


def choose_players():
    no_of_players = None
    while no_of_players not in ('1', '2'):
        no_of_players = input('\nNum of players 1/2?\n--> ').strip()

    player_name = choose_name('Player 1')
    player1 = Player(player_name)

    if no_of_players == '2':
        player_name = choose_name('Player 2')
        player2 = Player(player_name)
        play_game(player1, player2)

    play_game(player1)


def play_game(player1, player2=Player('Computer')):
    player2.choose_word('hangman') # TODO add functionality
    game = Game(player1, player2)

    while not game.winner:
        guess(game.player)
        game.check_player_guess()

    # TODO display winner

    if play_again():
        if player2.name == 'Computer':
            play_game(player1, Player('Computer'))
        else:
            # Switch game roles
            play_game(game.opponent, game.player)

    print('\nThanks for playing! See you again soon!') # TODO Add points etc?
    # Bug can print multiple times?


def guess(player):
    player_guess = input(f'\nGuess a letter or the word {player.name}!\n--> ')
    player.new_guess(player_guess)


def choose_name(player):
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


if __name__ == '__main__':
    print('\nWelcome to Hangman....')
    choose_players()
