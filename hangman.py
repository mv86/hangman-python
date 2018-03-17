#!/home/max/Python/projects/hangman/venv/bin/python
"""Script to start Hangman game."""
import sys
from game_objects import Game
from display import MSG
from hangman_helper import choose_players, choose_word, clear_screen, \
                           play, play_again


def hangman():
    """Entry point to game."""
    clear_screen()
    print(MSG['welcome'])
    player1, player2 = choose_players()
    new_game(player1, player2)
    

def new_game(player1, player2):
    """Hangman game loop."""
    choose_word(player2)
    game = Game(player1, player2)
    game.display_game_state()

    while not game.winner:
        play(game)

    print(MSG['winner'] % game.winner)

    if play_again():
        if player2.name == 'Computer':  # Computer always player 2
            new_game(player1, player2)
        else:  # Switch game roles
            new_game(game.opponent, game.player)

    print(MSG['goodbye'])


if __name__ == '__main__':
    try:
        hangman()
    except (KeyboardInterrupt, EOFError):
        print('\n')
        print(MSG['goodbye'])
        sys.exit(0)
