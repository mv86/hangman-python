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

    def __repr__(self):
        return f'{self.__class__.__name__!r}({self.name!r})'

    def __str__(self):
        return f'Player: Name = {self.name}'
