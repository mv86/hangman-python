#!/home/max/Python/projects/hangman/venv/bin/python
"""Script to start Hangman game."""
import sys
from game import Game
from game_colours import YELLOW, BLUE, END
from hangman_helper import choose_players, choose_word, clear_screen, \
                           prompt_for_guess, play_again


def hangman():
    """Entry point to game."""
    print(f'\n{YELLOW}Welcome to Hangman....\nPress Ctrl-C to exit at any time....\n{END}')
    player1, player2 = choose_players()
    clear_screen()
    play_game(player1, player2)
    print(f'\n{YELLOW}Thanks for playing! See you again soon!\n{END}')
    

def play_game(player1, player2):
    """Hangman game loop."""
    word = choose_word(player2)
    player2.add_word_choice(word)
    clear_screen()
    game = Game(player1, player2)
    game.display_board()

    while not game.winner:
        guess = prompt_for_guess(game)
        game.player.new_guess(guess)
        game.update_game()
        game.check_for_winner()
        clear_screen()
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
    try:
        hangman()
    except KeyboardInterrupt:
        print(f'\n\n{YELLOW}Thanks for playing! See you again soon!\n{END}')
        sys.exit(0)
    except EOFError:
        print(f'\n\n{YELLOW}Thanks for playing! See you again soon!\n{END}')
        sys.exit(0)
