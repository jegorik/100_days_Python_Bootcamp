import random


class GuessNumber:
    """A class to represent a number guessing game."""

    EASY = 'easy'
    HARD = 'hard'

    def __str__(self):
        """Return a string representation of the game title."""
        return """    
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __   
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|  
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   
        """

    def __init__(self):
        """Initialize the game with a number range and start the game."""
        self.range = range(1, 101)
        self.generated_number = 0
        self.range_start = self.range.start
        self.range_end = self.range.stop
        self.guess_number = 10
        print(
            f'{self}\nWelcome to the Number Guessing Game!\n' +
            f'I\'m thinking of a number between {self.get_range()}.')
        self.game_start()

    def game_start(self):
        """Start the game loop, generating a new number and handling user input."""
        while True:
            self.generated_number = self.generate_random_number()
            print(f'Generated number: {self.generated_number}')
            self.guess_number = 10
            difficulty = self.get_user_input('Choose a difficulty. Type \'easy\' or \'hard\': ', 'difficulty')
            if difficulty == self.HARD:
                self.guess_number = 5
            self.guessing()
            if self.continue_game() == 'n':
                break

    def guessing(self):
        """Handle the guessing logic for the user."""
        while True:
            if self.guess_number == 0:
                print(f'You\'ve run out of guesses. The number was {self.generated_number}. Game Over.')
                return
            else:
                print(f'You have {self.guess_number} guesses left.')
                user_guess = self.get_user_input('Make a guess: ', 'guessing')
                if user_guess == self.generated_number:
                    print(f'You got it right! The number was {user_guess}.')
                    return
                elif user_guess > self.generated_number:
                    self.guess_number -= 1
                    print('Too high.')
                elif user_guess < self.generated_number:
                    self.guess_number -= 1
                    print('Too low.')

    def get_user_input(self, prompt, step):
        """Get and validate user input based on the current step."""
        validation_map = {
            'difficulty': lambda x: x in [self.EASY, self.HARD],
            'guessing': lambda x: x.isdigit() and int(x) in self.range,
            'continue': lambda x: x in ['y', 'n']
        }
        while True:
            user_input = input(prompt).lower()
            if validation_map[step](user_input):
                return user_input if step != 'guessing' else int(user_input)
            else:
                print(self.get_error_message(step))

    def get_error_message(self, step):
        """Return an error message based on the input step."""
        messages = {
            'difficulty': 'Type \'easy\' or \'hard\'.',
            'guessing': f'Enter a valid number from {self.get_range()}.',
            'continue': 'Write \'y\' or \'n\''
        }
        return messages[step]

    def continue_game(self):
        """Ask the user if they want to start a new game."""
        return self.get_user_input('Start a new game? (y/n): ', 'continue')

    def generate_random_number(self):
        """Generate a random number within the defined range."""
        return random.randint(self.range_start, self.range_end)

    def get_range(self):
        """Return the current range of numbers as a string."""
        return f'{self.range_start} and {self.range_end}'


def main():
    """Main function to start the GuessNumber game."""
    guesser = GuessNumber()


if __name__ == '__main__':
    main()