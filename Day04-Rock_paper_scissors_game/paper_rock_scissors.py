import random


class Game:
    """A class to represent the Rock, Paper, Scissors game."""

    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    combinations = {
        ROCK: '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)        
        ''',
        PAPER: '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)        
        ''',
        SCISSORS: '''
    _______    
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
                '''
    }

    def start_game(self):
        """Starts the game loop, allowing the player to play multiple rounds."""
        while True:
            player_choice = self.get_player_input(
                'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n')
            opponent_choice = self.generate_random_number()
            self.check_winner(player_choice, opponent_choice)
            if not self.play_again():
                print("Thanks for playing!")
                break

    def get_player_input(self, prompt):
        """Prompts the player for input and validates it.

        Args:
            prompt (str): The message to display to the player.

        Returns:
            int: The validated player choice (0, 1, or 2).
        """
        while True:
            try:
                player_input = int(input(prompt))
                if self.validate_player_input(player_input):
                    return player_input
            except ValueError:
                print('Invalid input. Please choose a number from: 0, 1, or 2.')

    def validate_player_input(self, player_input):
        """Validates the player's input.

        Args:
            player_input (int): The player's choice.

        Returns:
            bool: True if the input is valid, False otherwise.
        """
        if player_input in (self.ROCK, self.PAPER, self.SCISSORS):
            return True
        else:
            print(f'{player_input} is not a valid number. Please choose 0, 1, or 2.')
            return False

    def generate_random_number(self):
        """Generates a random choice for the opponent.

        Returns:
            int: A random number representing the opponent's choice (0, 1, or 2).
        """
        return random.randint(self.ROCK, self.SCISSORS)

    def check_winner(self, player_choice, opponent_choice):
        """Determines the winner of the game and displays the result.

        Args:
            player_choice (int): The player's choice.
            opponent_choice (int): The opponent's choice.
        """
        print(f'You chose: {self.combinations[player_choice]}')
        print('Computer chose: ')
        print(self.combinations[opponent_choice])

        if player_choice == opponent_choice:
            print('It\'s a draw!')
        elif (player_choice == self.ROCK and opponent_choice == self.SCISSORS) or \
                (player_choice == self.SCISSORS and opponent_choice == self.PAPER) or \
                (player_choice == self.PAPER and opponent_choice == self.ROCK):
            print('You Win!')
        else:
            print('You Lose.')

    def play_again(self):
        """Asks the player if they want to play another round.

        Returns:
            bool: True if the player wants to play again, False otherwise.
        """
        return input("Do you want to play again? (yes/no): ").strip().lower() == 'yes'


def main():
    """Main function to start the game."""
    game = Game()
    game.start_game()


if __name__ == '__main__':
    main()