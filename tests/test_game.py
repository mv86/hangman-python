"""Test unit for Game class."""
import unittest
from player import Player
from game import Game


class TestGame(unittest.TestCase):
    """Test unit for Game class."""
    def setUp(self):
        self.player1 = Player('Max')
        self.player2 = Player('Mary')
        self.player2.choose_word('hangman')
        self.game = Game(self.player1, self.player2)

    def test_game_state_initialisation(self):
        self.assertEqual(self.player1, self.game.player)
        self.assertEqual(self.player2, self.game.opponent)
        self.assertEqual(['_', '_', '_', '_', '_', '_', '_'], self.game.word)
        self.assertEqual([], self.game.misses)
        self.assertEqual(None, self.game.winner)

    def test_check_player_guess(self):
        self.player1.new_guess('a')
        self.game.check_player_guess()
        self.assertEqual('A', self.game.player.guess)
        self.assertEqual(1, self.game.player.guesses)
        self.assertEqual(['_', 'A', '_', '_', '_', 'A', '_'], self.game.word)

        self.player1.new_guess('b')
        self.game.check_player_guess()
        self.assertEqual(2, self.game.player.guesses)
        self.assertEqual(['b'], self.game.misses)
        self.assertEqual(['_', 'A', '_', '_', '_', 'A', '_'], self.game.word)

        self.player1.new_guess('dangdan')
        self.assertEqual('DANGDAN', self.game.player.guess)
        self.game.check_player_guess()
        self.assertEqual(3, self.game.player.guesses)
        self.assertEqual(['b', 'dangdan'], self.game.misses)
        self.assertEqual(['_', 'A', '_', '_', '_', 'A', '_'], self.game.word)
        
    def test_player_wins(self):
        self.player1.new_guess('hangman')
        self.game.check_player_guess()
        self.assertEqual(['H', 'A', 'N', 'G', 'M', 'A', 'N'], self.game.word)     
        self.assertEqual('Max', self.game.winner)
        self.assertEqual(1, self.player1.points)

    def test_opponant_wins(self):
        self.game.misses = ['b', 'c', 'd', 'e', 'f', 'i', 'k', 'l']
        self.player1.new_guess('o')
        self.game.check_player_guess()
        self.assertEqual(['H', 'A', 'N', 'G', 'M', 'A', 'N'], self.game.word)
        self.assertEqual('Mary', self.game.winner)
        self.assertEqual(1, self.player2.points)
