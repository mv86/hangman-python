#!/home/max/Python/projects/hangman/venv/bin/python
"""Script to start Hangman game."""
from game import Game
from hangman_helper import choose_players, play_again


def hangman():
    print('\nWelcome to Hangman....')
    player1, player2 = choose_players()
    play_game(player1, player2)
    print('\nThanks for playing! See you again soon!\n')
    

def play_game(player1, player2):
    player2.choose_word('hangman') # TODO add functionality
    game = Game(player1, player2)
    game.display_board()

    while not game.winner:
        guess = input(f'\nGuess a letter or the word {game.player.name}!\n--> ')
        game.player.new_guess(guess)
        game.check_player_guess()
        game.display_board()

    print(f'{game.winner} wins!!!')

    if play_again():
        if player2.name == 'Computer':
            # Computer always player 2
            play_game(player1, player2)
        else:
            # Switch game roles
            play_game(game.opponent, game.player)


if __name__ == '__main__':
    hangman()
