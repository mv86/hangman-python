"""Test unit for Player class."""
import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    """Test unit for PLayer class."""
    def setUp(self):
        self.player = Player('Max')

    def test_player_initialisation(self):
        self.assertEqual('Max', self.player.name)
        self.assertEqual(0, self.player.guesses)
        self.assertEqual(0, self.player.points)
        self.assertEqual('', self.player.word)
        self.assertEqual('', self.player.guess)

    def test_choose_word(self):
        self.player.choose_word('hangman')
        self.assertEqual('HANGMAN', self.player.word)

    # def test_new_guess(self):
    #     self.player.new_guess('a')
    #     self.assertEqual('A', self.player.guess)
    #     self.assertEqual(1, self.player.guesses)
    #     self.player.new_guess('b')
    #     self.assertEqual(2, self.player.guesses)