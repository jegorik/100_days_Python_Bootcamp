class TipCalculator:
    """A simple tip calculator that calculates the amount each person should pay."""

    def __init__(self):
        """Initialize the TipCalculator and greet the user."""
        print('Welcome to the tip calculator!')

    def calculate_tip_per_person(self):
        """Calculate the amount each person should pay based on the total bill, tip percentage, and number of people.

        Returns:
            str: A formatted string indicating the amount each person should pay.
        """
        total_bill = self.get_positive_input('What was the total bill? $')
        tip_amount = self.get_positive_input('How much tip would you like to give? (in percentage): ')
        parts_to_split = self.get_positive_input('How many people to split the bill? ')

        # Calculate the total amount including tip
        total_with_tip = total_bill * (1 + tip_amount / 100)
        # Calculate the amount each person should pay
        amount_per_person = total_with_tip / parts_to_split

        return f'Each person should pay: ${round(amount_per_person, 2)}'

    def get_positive_input(self, prompt):
        """Prompt the user for input until a valid non-negative number is provided.

        Args:
            prompt (str): The message to display when asking for input.

        Returns:
            float: The validated user input as a float.
        """
        while True:
            try:
                user_input = float(input(prompt))
                if user_input < 0:
                    raise ValueError("Input must be a non-negative number.")
                return user_input
            except ValueError as e:
                print(f'Invalid input: {e}. Please input numbers only.')


def main():
    """Main function to run the tip calculator."""
    tip_calculator = TipCalculator()
    print(tip_calculator.calculate_tip_per_person())


if __name__ == '__main__':
    main()