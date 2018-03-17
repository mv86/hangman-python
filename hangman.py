#!/home/max/Python/projects/hangman/venv/bin/python
"""Script to start Hangman game."""
from game_objects import Game
from display import MSG
from hangman_helper import start_game, choose_players, choose_word, \
                           play, play_again, end_game


def hangman():
    """Entry point to game."""
    start_game()
    player1, player2 = choose_players()
    new_game(player1, player2)
    

def new_game(player1, player2):
    """Hangman game loop."""
    choose_word(player2)
    game = Game(player1, player2)

    while not game.winner:
        play(game)

    print(MSG['winner'] % game.winner)

    if play_again():
        if player2.name == 'Computer':  # Computer always player 2
            new_game(player1, player2)
        else:  # Switch game roles
            new_game(game.opponent, game.player)

    end_game()


if __name__ == '__main__':
    try:
        hangman()
    except (KeyboardInterrupt, EOFError):
        end_game()
