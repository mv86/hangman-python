"""Player Class."""


class Player():
    """Player class"""
    def __init__(self, name):
        self.name = name
        self.guesses = 0
        self.points = 0
        self.word = ''
        self.guess = ''

    def __repr__(self):
        return f'{self.__class__.__name__!r}({self.name!r})'

    def __str__(self):
        return f'Player: Name = {self.name}'

    def choose_word(self, word):
        self.word = word.upper()

    def new_guess(self):
        guess = input(f'\nGuess a letter or the word {self.name}!\n--> ')
        self.guess = guess.upper()
        self.guesses += 1
