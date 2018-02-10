"""Test unit for GameState class."""
import unittest
from player import Player
from game_state import GameState


class TestGameState(unittest.TestCase):
    """Test unit for GameState class."""
    def setUp(self):
        self.player1 = Player('Max')
        self.player2 = Player('Mary')
        self.player2.choose_word('hangman')
        self.game_state = GameState(self.player1, self.player2)

    def test_game_state_initialisation(self):
        self.assertEqual(self.player1, self.game_state.player)
        self.assertEqual(self.player2, self.game_state.opponent)
        self.assertEqual(['_', '_', '_', '_', '_', '_', '_'], self.game_state.word)
        self.assertEqual('', self.game_state.board_image)
        self.assertEqual('', self.game_state.winner)

    def test_check_player_guess(self):
        self.player1.new_guess('a')
        self.game_state.check_player_guess()
        self.assertEqual('A', self.game_state.player.guess)
        self.assertEqual(1, self.game_state.player.guesses)
        self.assertEqual(['_', 'A', '_', '_', '_', 'A', '_'], self.game_state.word)

        self.player1.new_guess('b')
        self.assertEqual('B', self.game_state.player.guess)
        self.game_state.check_player_guess()
        self.assertEqual(2, self.game_state.player.guesses)
        self.assertEqual(['b'], self.game_state.player.misses)
        self.assertEqual(['_', 'A', '_', '_', '_', 'A', '_'], self.game_state.word)

        self.player1.new_guess('dangdan')
        self.assertEqual('DANGDAN', self.game_state.player.guess)
        self.game_state.check_player_guess()
        self.assertEqual(3, self.game_state.player.guesses)
        self.assertEqual(['b', 'dangdan'], self.game_state.player.misses)
        self.assertEqual(['_', 'A', '_', '_', '_', 'A', '_'], self.game_state.word)
        
        self.player1.new_guess('hangman')
        self.assertEqual('HANGMAN', self.game_state.player.guess)
        self.game_state.check_player_guess()
        self.assertEqual(4, self.game_state.player.guesses)
        self.assertEqual(['b', 'dangdan'], self.game_state.player.misses)
        self.assertEqual(['H', 'A', 'N', 'G', 'M', 'A', 'N'], self.game_state.word)     
