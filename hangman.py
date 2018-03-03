#!/home/max/Python/projects/hangman/venv/bin/python
"""Script to start Hangman game."""
import sys
from game import Game
from display import BLUE, END, MSG
from hangman_helper import choose_players, choose_word, clear_screen, \
                           prompt_for_guess, play_again


def hangman():
    """Entry point to game."""
    clear_screen()
    print(MSG['welcome'])
    player1, player2 = choose_players()
    play_game(player1, player2)
    print(MSG['goodbye'])
    

def play_game(player1, player2):
    """Hangman game loop."""
    clear_screen()
    word = choose_word(player2)
    player2.add_word_choice(word)
    clear_screen()
    game = Game(player1, player2)
    game.display_game_state()

    while not game.winner:
        guess = prompt_for_guess(game)
        game.player.new_guess(guess)
        game.update_game()
        game.check_for_winner()
        clear_screen()
        game.display_game_state()

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
    except (KeyboardInterrupt, EOFError):
        print('\n')
        print(MSG['goodbye'])
        sys.exit(0)
