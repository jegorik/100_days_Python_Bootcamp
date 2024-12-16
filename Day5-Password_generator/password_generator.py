import string
from random import choices, shuffle


class PasswordGenerator:
    """A class to generate strong passwords based on user-defined criteria."""

    def __init__(self):
        """Initialize the PasswordGenerator with character sets for password creation."""
        self.alphabet = list(string.ascii_letters)  # List of uppercase and lowercase letters
        self.symbols = list('!@#$%^&*()-+=:`~?|;:,"<>[]{}')  # List of common symbols
        self.numbers = list(string.digits)  # List of digits from 0 to 9
        print('Welcome to Password Generator!')

    def create_password(self):
        """Prompt the user for password criteria and generate a password."""
        num_of_letters = self.get_user_input('How many letters would you like in your password?\n')
        num_of_symbols = self.get_user_input('How many symbols would you like?\n')
        num_of_numbers = self.get_user_input('How many numbers would you like?\n')

        # Generate and display the password based on user input
        password = self.generate_password(num_of_letters, num_of_symbols, num_of_numbers)
        print(password)

    def get_user_input(self, prompt: str) -> int:
        """Get a valid integer input from the user.

        Args:
            prompt (str): The prompt message to display to the user.

        Returns:
            int: A non-negative integer input from the user.
        """
        while True:
            try:
                user_input = int(input(prompt))
                if user_input < 0:
                    raise ValueError("Input must be a non-negative integer.")
                return user_input
            except ValueError as e:
                print(e)  # Display error message for invalid input

    def generate_password(self, num_of_letters: int, num_of_symbols: int, num_of_numbers: int) -> str:
        """Generate a random password based on specified criteria.

        Args:
            num_of_letters (int): The number of letters in the password.
            num_of_symbols (int): The number of symbols in the password.
            num_of_numbers (int): The number of numbers in the password.

        Returns:
            str: The generated password.
        """
        # Create a list of characters based on user specifications
        result_list = (
                choices(self.alphabet, k=num_of_letters) +
                choices(self.symbols, k=num_of_symbols) +
                choices(self.numbers, k=num_of_numbers)
        )

        # Shuffle the result list to ensure randomness
        shuffle(result_list)
        password = ''.join(result_list)  # Join the list into a single string
        return f'Your password is: {password}'


def main():
    """Main function to run the Password Generator."""
    password_generator = PasswordGenerator()  # Create an instance of PasswordGenerator
    password_generator.create_password()  # Start the password creation process


if __name__ == '__main__':
    main()  # Execute the main function