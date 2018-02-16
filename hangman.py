#!/home/max/Python/projects/hangman/venv/bin/python
"""Script to start Hangman game."""
from game import Game
from hangman_helper import choose_players, choose_word, validate_player_guess, play_again
from game_colours import YELLOW, BLUE, END

# TODO Add functionality to exit game early

def hangman():
    """Entry point to game."""
    print(f'\n{YELLOW}Welcome to Hangman....\n{END}')
    player1, player2 = choose_players()
    play_game(player1, player2)
    print(f'\n{YELLOW}Thanks for playing! See you again soon!\n{END}')
    

def play_game(player1, player2):
    """Hangman game loop."""
    word = choose_word(player2)
    player2.add_word_choice(word)
    game = Game(player1, player2)
    game.display_board()

    while not game.winner:
        guess = validate_player_guess(game)
        game.player.new_guess(guess)
        game.check_player_guess()
        game.check_for_winner()
        game.display_board()

    print(f'{BLUE}{game.winner} wins!!!\n{END}')

    if play_again():
        if player2.name == 'Computer':
            # Computer always player 2
            play_game(player1, player2)
        else:
            # Switch game roles
            play_game(game.opponent, game.player)


if __name__ == '__main__':
    hangman()
