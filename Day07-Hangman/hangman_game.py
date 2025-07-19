from random import choice


class Game:
    """
    A class to represent the Hangman game.
    """

    GAME_PICTURES = {
        'logo': """
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/
        """,
        'hangman6': """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        'hangman5': """
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        """,
        'hangman4': """
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========
        """,
        'hangman3': """
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        """,
        'hangman2': """
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========
        """,
        'hangman1': """
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
    """,
        'hangman0': """
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
    """
    }

    WORD_LIST = ('resins', 'orange', 'computer', 'airplane', 'litterbox')
    MAX_LIVES = 6

    def __init__(self):
        """
        Initializes the game with a random word to guess,
        sets the number of lives, and displays the game logo.
        """
        self.word_to_guess = ''
        self.guessed_letters = []
        self.player_lives = self.MAX_LIVES
        print(self.GAME_PICTURES['logo'])

    def start_game(self):
        """
        Starts the game by selecting a random word from the word list
        and initializing the guessed letters.
        """
        self.word_to_guess = choice(self.WORD_LIST)
        self.guessed_letters = ['_'] * len(self.word_to_guess)
        self.word_guess()

    def word_guess(self):
        """
        Main loop for guessing letters. Prompts the player for input
        and checks the guessed letters until the game ends.
        """
        while True:
            print(f'Word to guess: {" ".join(self.guessed_letters)}')
            player_guess = input('Guess a letter: ').lower()

            # Validate the player's guess
            if not self.is_valid_guess(player_guess):
                print("Please enter a single alphabetical character.")
                continue

            self.check_player_guess(player_guess)
            self.game_status()
            self.print_hangman()
            self.print_footer(' ')

    def is_valid_guess(self, guess):
        """
        Validates the player's guess to ensure it is a single alphabetical character.

        Args:
            guess (str): The player's guessed letter.

        Returns:
            bool: True if the guess is valid, False otherwise.
        """
        return len(guess) == 1 and guess.isalpha()

    def check_player_guess(self, player_guess):
        """
        Checks the player's guess against the word to guess. Updates the
        guessed letters or reduces the player's lives if the guess is incorrect.

        Args:
            player_guess (str): The player's guessed letter.
        """
        if player_guess in self.guessed_letters:
            print(f'You\'ve already guessed {player_guess}')
            return

        if player_guess in self.word_to_guess:
            # Update guessed letters with the correct guess
            for index, letter in enumerate(self.word_to_guess):
                if letter == player_guess:
                    self.guessed_letters[index] = player_guess
        else:
            print(f'You guessed {player_guess}, that\'s not in the word. You lose a life.')
            self.player_lives -= 1

    def game_status(self):
        """
        Checks the current game status to determine if the player has won or lost.
        """
        if self.player_lives == 0:
            self.print_hangman()
            self.print_footer('YOU LOSE')
            exit()
        elif '_' not in self.guessed_letters:
            self.print_footer('YOU WON')
            exit()

    def print_hangman(self):
        """
        Displays the current state of the hangman based on the number of lives left.
        """
        print(self.GAME_PICTURES[f'hangman{self.player_lives}'])

    def print_footer(self, status):
        """
        Prints the footer message indicating the game result or remaining lives.

        Args:
            status (str): The status of the game ('YOU WON' or 'YOU LOSE').
        """
        if status in ('YOU WON', 'YOU LOSE'):
            print(f"{'*' * 16} IT WAS {self.word_to_guess}! {status} {'*' * 16}")
        else:
            print(f"{'*' * 16} {self.player_lives}/{self.MAX_LIVES} LIVES LEFT {'*' * 16}")


def main():
    """
    Main function to start the Hangman game.
    """
    new_game = Game()
    new_game.start_game()


if __name__ == '__main__':
    main()
