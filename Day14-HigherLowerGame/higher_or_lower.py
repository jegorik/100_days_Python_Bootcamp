import art
import game_data
import random
from typing import Dict, List, Tuple, Any


class HigherLower:
    """A Higher Lower game where players guess which celebrity/entity has more followers."""

    def __init__(self):
        """Initialize the game with data and starting values."""
        self.data: List[Dict[str, Any]] = game_data.data
        self.score: int = 0
        self.is_game_active: bool = True
        
        # Validate that we have enough data to play
        if len(self.data) < 2:
            raise ValueError("Need at least 2 entries in game data to play")

    def start_game(self) -> None:
        """Start and run the main game loop."""
        print(art.logo)
        print("Welcome to the Higher Lower Game!")
        
        while self.is_game_active:
            choice_a, choice_b = self.get_random_pair()
            self.display_comparison(choice_a, choice_b)
            
            player_guess = self.get_player_input()
            self.check_answer(choice_a, choice_b, player_guess)

    def get_random_pair(self) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """Get two different random entries from the game data.
        
        Returns:
            Tuple of two different dictionary entries from game data.
        """
        choice_a = random.choice(self.data)
        choice_b = random.choice(self.data)
        
        # Ensure we get two different choices
        while choice_a == choice_b:
            choice_b = random.choice(self.data)
            
        return choice_a, choice_b

    def display_comparison(self, choice_a: Dict[str, Any], choice_b: Dict[str, Any]) -> None:
        """Display the two choices for comparison.
        
        Args:
            choice_a: First choice dictionary
            choice_b: Second choice dictionary
        """
        print(f"\nCompare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}\n"
             f"{art.vs}\n"
             f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}\n")

    def get_player_input(self) -> str:
        """Get valid player input (A or B).
        
        Returns:
            Player's choice as lowercase string ('a' or 'b')
        """
        while True:
            player_choice = input("Who has more followers? Type 'A' or 'B': ").strip().lower()
            if player_choice in ['a', 'b']:
                return player_choice
            print("Invalid input! Please choose 'A' or 'B'")

    def check_answer(self, choice_a: Dict[str, Any], choice_b: Dict[str, Any], player_guess: str) -> None:
        """Check if the player's answer is correct and update game state.
        
        Args:
            choice_a: First choice dictionary
            choice_b: Second choice dictionary
            player_guess: Player's guess ('a' or 'b')
        """
        followers_a = choice_a['follower_count']
        followers_b = choice_b['follower_count']
        
        # Determine the correct answer
        correct_choice = 'a' if followers_a > followers_b else 'b'
        higher_count = max(followers_a, followers_b)
        
        if player_guess == correct_choice:
            self.score += 1
            print(f"\nYou're right! Current score: {self.score}")
            print(f"The answer was {higher_count} million followers.")
        else:
            self.is_game_active = False
            print(f"\nSorry, that's wrong. Final score: {self.score}")
            print(f"The correct answer was {higher_count} million followers.")
            
        # Add a separator for better readability
        if self.is_game_active:
            print("-" * 50)


def main() -> None:
    """Main function to run the Higher Lower game."""
    try:
        game = HigherLower()
        game.start_game()
        print("\nThanks for playing!")
    except ValueError as e:
        print(f"Game initialization error: {e}")
    except KeyboardInterrupt:
        print("\nGame interrupted by user. Thanks for playing!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
