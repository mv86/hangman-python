#!/home/max/Python/projects/hangman/venv/bin/python
"""Script to start Hangman game."""
from player import Player
from game import Game
from hangman_helper import choose_players, play_again


def hangman():
    print('\nWelcome to Hangman....')
    player1, player2 = choose_players()
    play_game(player1, player2)
    print('\nThanks for playing! See you again soon!\n') # TODO Add points etc?
    

def play_game(player1, player2):
    player2.choose_word('hangman') # TODO add functionality
    game = Game(player1, player2)
    game.show_board()

    while not game.winner:
        game.player.new_guess()
        game.check_player_guess()
        game.show_board()

    # TODO display winner

    if play_again():
        if player2.name == 'Computer':
            play_game(player1, Player('Computer'))
        else:
            # Switch game roles
            play_game(game.opponent, game.player)


if __name__ == '__main__':
    hangman()
