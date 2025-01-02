class Calculator:
    def __str__(self):
        """Return the logo of the calculator."""
        return """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
        """

    def __init__(self):
        """Initialize the calculator with operations and display the logo."""
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        self.current_operation = ''
        self.sum = ''
        print(self)

    def start_calculations(self):
        """Start the calculation loop, prompting the user for input."""
        while True:
            self.get_user_input()

    def get_user_input(self):
        """Get user input for the first number, operation, and second number."""
        first_number = self.sum if self.sum else self.validate_input('What\'s the first number?: ', 'digit')
        operation = self.validate_input('Pick an operation: ', 'operation')
        second_number = self.validate_input('What\'s the second number?: ', 'digit')
        self.sum = operation(first_number, second_number)
        self.continue_work(
            f'Type \'y\' to continue calculating with {self.sum}, or type \'n\' to start a new calculation or \'q\' to quit: ',
            ['y', 'n', 'q'])

    def validate_input(self, prompt: str, input_type: str):
        """Validate user input based on the expected type (digit or operation)."""
        while True:
            if input_type == 'operation':
                print("Available operations:")
                for key in self.operations.keys():
                    print(key)
                user_input = input(prompt)
                if user_input in self.operations:
                    self.current_operation = user_input
                    return self.operations[user_input]
                else:
                    print('Please choose an operation from the list.')
            elif input_type == 'digit':
                try:
                    user_input = float(input(prompt))
                    return user_input
                except ValueError:
                    print('Please input digits only.')

    def continue_work(self, prompt: str, valid_options: list):
        """Prompt the user to continue, start a new calculation, or quit."""
        while True:
            user_input = input(prompt).lower()
            if user_input in valid_options:
                if user_input == 'n':
                    self.sum = ''
                    break
                elif user_input == 'q':
                    exit()
                else:
                    break
            else:
                print('Choose \'y\', \'n\' or \'q\'.')

    def perform_operation(self, first_number: float, second_number: float) -> float:
        """Perform the current operation on the two numbers and print the result."""
        result = self.current_operation(first_number, second_number)
        self.print_result(first_number, second_number, self.current_operation, result)
        return result

    def add(self, first_number: float, second_number: float) -> float:
        """Return the sum of two numbers."""
        return first_number + second_number

    def subtract(self, first_number: float, second_number: float) -> float:
        """Return the difference of two numbers."""
        return first_number - second_number

    def multiply(self, first_number: float, second_number: float) -> float:
        """Return the product of two numbers."""
        return first_number * second_number

    def divide(self, first_number: float, second_number: float) -> float:
        """Return the quotient of two numbers, handling division by zero."""
        if second_number == 0:
            print("Error: Division by zero is not allowed.")
            return first_number  # Return the first number unchanged
        return first_number / second_number

    def print_result(self, first_number: float, second_number: float, operation: str, result: float):
        """Print the result of the calculation."""
        print(f'{first_number} {operation} {second_number} = {result}')


def main():
    """Main function to run the calculator."""
    calculator = Calculator()
    calculator.start_calculations()


if __name__ == '__main__':
    main()