"""Test unit for Game class."""
import unittest
from player import Player
from game import Game


class TestGame(unittest.TestCase):
    """Test unit for Game class."""
    def setUp(self):
        self.player1 = Player('Max')
        self.player2 = Player('Mary')
        self.player2.add_word_choice('hangman')
        self.game = Game(self.player1, self.player2)

    def test_game_state_initialisation(self):
        self.assertEqual(self.player1, self.game.player)
        self.assertEqual(self.player2, self.game.opponent)
        self.assertEqual(['_', '_', '_', '_', '_', '_', '_'], self.game.word)
        self.assertEqual([], self.game.misses)
        self.assertEqual(None, self.game.winner)

    def test_validate_player_guess(self):
        self.game.word = ['_', 'A', '_', '_']
        self.game.misses = ['b']
        valid_guess, msg = self.game.validate_player_guess('')
        self.assertFalse(valid_guess)
        self.assertEqual('\033[91mMust be alphabetical characters!\033[0m', msg)
        valid_guess, msg = self.game.validate_player_guess(',')
        self.assertFalse(valid_guess)
        self.assertEqual('\033[91mMust be alphabetical characters!\033[0m', msg)
        valid_guess, msg = self.game.validate_player_guess('abc')
        self.assertFalse(valid_guess)
        self.assertEqual('\033[91mGuess a single letter or the entire word!\033[0m', msg)
        valid_guess, msg = self.game.validate_player_guess('b')
        self.assertFalse(valid_guess)
        self.assertEqual('\033[91mAlready tried that one, guess again!\033[0m', msg)
        valid_guess, msg = self.game.validate_player_guess('c')
        self.assertTrue(valid_guess)
        self.assertFalse(msg)

    def test_update_game(self):
        self.player1.new_guess('a')
        self.game.update_game()
        self.assertEqual('A', self.game.player.guess)
        self.assertEqual(1, self.game.player.guesses)
        self.assertEqual(['_', 'A', '_', '_', '_', 'A', '_'], self.game.word)

        self.player1.new_guess('b')
        self.game.update_game()
        self.assertEqual(2, self.game.player.guesses)
        self.assertEqual(['b'], self.game.misses)
        self.assertEqual(['_', 'A', '_', '_', '_', 'A', '_'], self.game.word)

        self.player1.new_guess('dangdan')
        self.assertEqual('DANGDAN', self.game.player.guess)
        self.game.update_game()
        self.assertEqual(3, self.game.player.guesses)
        self.assertEqual(['b', 'dangdan'], self.game.misses)
        self.assertEqual(['_', 'A', '_', '_', '_', 'A', '_'], self.game.word)
        
    def test_player_wins(self):
        self.player1.new_guess('hangman')
        self.game.update_game()
        self.game.check_for_winner()
        self.assertEqual(['H', 'A', 'N', 'G', 'M', 'A', 'N'], self.game.word)     
        self.assertEqual('Max', self.game.winner)
        self.assertEqual(1, self.player1.points)

    def test_opponant_wins(self):
        self.game.misses = ['b', 'c', 'd', 'e', 'f', 'i', 'k', 'l']
        self.player1.new_guess('o')
        self.game.update_game()
        self.game.check_for_winner()
        self.assertEqual(['H', 'A', 'N', 'G', 'M', 'A', 'N'], self.game.word)
        self.assertEqual('Mary', self.game.winner)
        self.assertEqual(1, self.player2.points)
