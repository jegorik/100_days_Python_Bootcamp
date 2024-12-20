import string


class Cipher:
    logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   

                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88
"""

    ACTIONS = ['encode', 'decode']

    def __init__(self):
        """Initialize the Cipher class with the alphabet and display the logo."""
        self.alphabet = list(string.ascii_lowercase)  # List of lowercase letters
        self.alphabet_length = len(self.alphabet)  # Length of the alphabet
        print(self.logo)

    def start(self):
        """Start the cipher process, allowing the user to encode or decode messages."""
        while True:
            action = self.get_valid_input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n', self.ACTIONS)
            data_to_process = self.get_string_data()  # Get the string and shift number from the user
            result = self.process_data(action, data_to_process)  # Process the data based on the action
            print(result)  # Output the result
            self.proceed()  # Ask if the user wants to continue

    def get_valid_input(self, prompt: str, valid_options: list) -> str:
        """Get valid input from the user based on the provided prompt and valid options.

        Args:
            prompt (str): The message to display to the user.
            valid_options (list): A list of valid input options.

        Returns:
            str: The valid input provided by the user.
        """
        while True:
            user_input = input(prompt).lower()  # Get user input and convert to lowercase
            if user_input in valid_options:
                return user_input  # Return valid input
            print(f'Choose from {", ".join(valid_options)}')  # Prompt user to choose a valid option

    def get_string_data(self) -> dict:
        """Get the string and shift number from the user.

        Returns:
            dict: A dictionary containing the string to process and the shift number.
        """
        while True:
            string_to_process = input('Type your message:\n').lower()  # Get the message from the user
            if not string_to_process:
                print('Input can\'t be empty.')  # Ensure input is not empty
                continue
            shift_number = self.get_shift_number(f'Type the shift number. Choose from 0 to {self.alphabet_length}:\n')
            return {'string': string_to_process, 'shift_number': shift_number}  # Return the data as a dictionary

    def get_shift_number(self, prompt: str) -> int:
        """Get a valid shift number from the user.

        Args:
            prompt (str): The message to display to the user.

        Returns:
            int: A valid shift number within the range of the alphabet length.
        """
        while True:
            try:
                shift_number = int(input(prompt))  # Get user input and convert to integer
                if 0 <= shift_number < self.alphabet_length:
                    return shift_number  # Return valid shift number
                print(f'{shift_number} is not in range 0 to {self.alphabet_length - 1}')  # Prompt if out of range
            except ValueError:
                print('Only numbers allowed.')  # Handle non-integer input

    def process_data(self, action: str, data: dict) -> str:
        """Process the input data based on the action (encode or decode).

        Args:
            action (str): The action to perform ('encode' or 'decode').
            data (dict): The data containing the string and shift number.

        Returns:
            str: The processed string after encoding or decoding.
        """
        shift = data['shift_number']
        result = []  # Use a list to collect results for efficiency
        for letter in data['string']:
            if letter in self.alphabet:  # Ensure only letters are processed
                # Calculate new position based on action
                position = (self.alphabet.index(letter) + shift) % self.alphabet_length if action == 'encode' else (self.alphabet.index(letter) - shift) % self.alphabet_length
                result.append(self.alphabet[position])  # Append the encoded/decoded letter
            else:
                result.append(letter)  # Keep non-alphabet characters unchanged
        return ''.join(result)  # Join the list into a single string

    def proceed(self):
        """Ask the user if they want to continue or exit the program."""
        user_choice = self.get_valid_input('Type \'yes\' if you want to go again. Otherwise type \'no\'.\n',['yes', 'no'])
        if user_choice == 'no':
            exit()  # Exit the program


def main():
    """Main function to run the Cipher program."""
    cipher = Cipher()  # Create an instance of the Cipher class
    cipher.start()  # Start the cipher process


if __name__ == '__main__':
    main()  # Run the main function