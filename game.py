"""Module with one class: Game"""
from board_images import BOARD_IMAGES


class Game():
    """Game class."""
    def __init__(self, player1, player2):
        self.player = player1
        self.opponent = player2
        self.word = list('_' * len(self.opponent.word))
        self.misses = []
        self.winner = None

    def __repr__(self):
        return f'{self.__class__.__name__!r}({self.player!r}, {self.opponent!r})'

    def __str__(self):
        return f'Game: Player = {self.player}, Opponent = {self.opponent}'

    def check_player_guess(self):
        """Internal logic for Game class. 

           Check player current guess and updates Game word, misses, and winner instance variables.
           Update player or opponent points when game ends.
        """
        guess = self.player.guess
        word = self.opponent.word
        player = self.player
        opponent = self.opponent

        # General single letter guess
        if len(guess) == 1 and self.word.count('_') > 1:
            if guess in word:
                self._update_game_word(guess, word)
            else:
                self.misses.append(guess.lower())

        # Single letter guess for final blank
        elif len(guess) == 1 and self.word.count('_') == 1:
            if guess in word:
                self._update_game_word(guess, word)
                self.winner = player.name
                player.points += 1
            else:
                self.misses.append(guess.lower())

        # Guess for whole word
        else:
            if guess == word:
                self.word = list(word)
                self.winner = player.name
                player.points += 1
            else:
                self.misses.append(guess.lower())
           
        # Check if guess limit has been reached     
        if len(self.misses) == 9:
            self.winner = opponent.name
            opponent.points += 1
            self.word = list(word)

    def display_board(self):
        """Display game progress to terminal: Board_image, word, misses and players points."""
        player = self.player
        opponent = self.opponent
        print(f"{BOARD_IMAGES[len(self.misses)]}")
        print(f"Word: {' '.join(self.word)}\n")
        print(f"Misses: {', '.join(self.misses)}\n")
        print(f"Points: {player.name} = {player.points}, {opponent.name} = {opponent.points}\n")

    def _update_game_word(self, guess, word):
        """Helper function for check player guess."""
        for idx, letter in enumerate(word):
            if guess == letter:
                self.word[idx] = guess
