"""Module with one class: Game."""
from board_images import BOARD_IMAGES
from game_colours import RED, YELLOW, END


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

    def validate_player_guess(self, guess):
        """Validate guess is a single letter or word guess and hasn't been guessed before. 

           Return True, None or False, str(err_msg).
        """
        if not guess.isalpha():
            msg = f'{RED}Must be alphabetical characters!{END}'
            return False, msg
        if len(guess) > 1 and len(guess) < len(self.word):
            msg = f'{RED}Guess a single letter or the entire word!{END}'
            return False, msg
        if guess.upper() in self.word or guess.lower() in self.misses:
            msg = f'{RED}Already tried that one, guess again!{END}'
            return False, msg
        return True, None

    def update_game(self):
        """Check player current guess and updates Game word, misses, & winner instance variables."""
        guess = self.player.guess
        word = self.opponent.word

        if len(guess) == 1:
            if guess in word:
                self._update_game_word(guess, word)
            else:
                self.misses.append(guess.lower())
        else:
            if guess == word:
                self.word = list(word)
            else:
                self.misses.append(guess.lower())
    
    def _update_game_word(self, guess, word):
        """Helper function for check player guess."""
        for idx, letter in enumerate(word):
            if guess == letter:
                self.word[idx] = guess

    def check_for_winner(self):
        """If winner, add point to correct player and set name to self.winner."""
        # Check if all letters guessed correctly
        if '_' not in self.word:
            self.winner = self.player.name
            self.player.points += 1
        # Check if guess limit has been reached     
        if len(self.misses) == 9:
            self.winner = self.opponent.name
            self.opponent.points += 1
            self.word = list(self.opponent.word)

    def display_board(self):
        """Display game progress to terminal: Board_image, word, misses and players points."""
        player = self.player
        opponent = self.opponent
        print(f"{BOARD_IMAGES[len(self.misses)]}")
        print(f"{YELLOW}Word: {' '.join(self.word)}\n{END}")
        print(f"{YELLOW}Misses: {', '.join(self.misses)}\n{END}")
        print(f"{YELLOW}Points: {player.name} = {player.points}, {opponent.name} = {opponent.points}\n{END}")
