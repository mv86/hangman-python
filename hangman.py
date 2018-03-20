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


def new_game(player, opponent):
    """Hangman game loop."""
    choose_word(opponent)
    game = Game(player, opponent)

    while not game.winner:
        play(game)

    print(MSG['winner'] % game.winner)

    if play_again():
        if opponent.name == 'Computer':  # Computer always opponent
            new_game(player, opponent)
        else:  # Switch game roles
            new_game(opponent, player)

    end_game()


if __name__ == '__main__':
    try:
        hangman()
    except (KeyboardInterrupt, EOFError):
        end_game()
