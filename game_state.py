"""GameState class."""


class GameState():
    """GameState class."""
    def __init__(self, player1, player2):
        self.player = player1
        self.opponent = player2
        self.word = list('_' * len(self.opponent.word))
        self.board_image = ''
        self.winner = ''

    def __repr__(self):
        return f'{self.__class__.__name__!r}({self.player!r}, {self.opponent!r})'

    def __str__(self):
        return f'GameState: Player = {self.player}, Opponent = {self.opponent}'

    def check_player_guess(self):
        self.player.guesses += 1
        guess = self.player.guess
        
        if len(guess) == 1 and self.word.count('_') > 1:
            if guess in self.opponent.word:
                self.word = [guess if guess == letter else '_' for letter in self.opponent.word]
            else:
                self.player.misses.append(guess.lower())

        elif len(guess) == 1 and self.word.count('_') == 1:
            if guess in self.opponent.word:
                # call game_over()
                # TODO move this functionality to game_over()
                self.word = [guess if guess == letter else '_' for letter in self.opponent.word]
            else:
                self.player.misses.append(guess.lower())

        else:
            if guess == self.opponent.word:
                #call game_over()
                #TODO move this funtionality to game_over
                self.word = list(self.opponent.word)
            else:
                self.player.misses.append(guess.lower())
