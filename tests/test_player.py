"""Test unit for Player class."""
import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    """Test unit for PLayer class."""
    def setUp(self):
        self.player = Player('Max')

    def test_player_setup(self):
        self.assertEqual('Max', self.player.name)
        self.assertEqual(9, self.player.guesses)
        self.assertEqual(0, self.player.points)
        self.assertEqual('', self.player.word)
        self.assertEqual('', self.player.guess)
        self.assertEqual([], self.player.misses)

    def test_choose_word(self):
        self.player.choose_word('hangman')
        self.assertEqual('hangman', self.player.word)