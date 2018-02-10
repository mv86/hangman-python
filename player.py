"""Player Class."""

class Player():
    """Player class"""
    def __init__(self, name):
        self.name = name
        self.guesses = 9
        self.points = 0
        self.word = ''
        self.guess = ''
        self.misses = []
