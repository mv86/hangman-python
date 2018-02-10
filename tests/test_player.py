"""Test unit for Player class."""
import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    """Test unit for PLayer class."""
    # def __init__(self):
    #     self.player = Player('Max')

    def test_player_setup(self):
        player = Player('Max')
        self.assertEqual('Max', player.name)
        self.assertEqual(9, player.guesses)
        self.assertEqual(0, player.points)
        self.assertEqual('', player.word)
        self.assertEqual('', player.guess)
        self.assertEqual([], player.misses)
