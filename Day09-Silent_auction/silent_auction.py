class SilentAuction:
    """
    A class to represent a silent auction where users can place bids.

    Attributes:
        logo (str): A string representation of the auction logo.
        bids (list): A list to store bids as tuples of (username, bid).
        name_counter (dict): A dictionary to keep track of how many times each name has been used.
    """
    logo = """
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
    """

    def __init__(self):
        """Initializes the SilentAuction with an empty list of bids and a name counter."""
        self.bids = []  # Initialize bids as an empty list
        self.name_counter = {}  # Dictionary to keep track of name counts

    def start_auction(self):
        """Starts the auction process, allowing users to place bids."""
        print(self.logo)  # Display the auction logo
        while True:
            self.get_user_input()  # Get user input for bids
            if not self.proceed_auction():  # Check if there are more bidders
                break  # Exit the auction loop if no more bidders

    def get_user_input(self):
        """Prompts the user for their name and bid, and stores the bid."""
        username = self.validate_input('What is your name?: ', 'name')  # Validate and get username
        bid = self.validate_input('What is your bid?: $', 'bid')  # Validate and get bid amount

        # Create a unique identifier for the user
        if username in self.name_counter:
            self.name_counter[username] += 1  # Increment the count for the name
        else:
            self.name_counter[username] = 1  # Initialize the count for the name

        unique_name = f"{username} Nr{self.name_counter[username]}"  # Create a unique name
        self.bids.append((unique_name, bid))  # Store bid as a tuple (unique_name, bid)

    def validate_input(self, prompt, input_type):
        """Validates user input for name and bid.

        Args:
            prompt (str): The prompt message to display to the user.
            input_type (str): The type of input to validate ('name' or 'bid').

        Returns:
            str or int: The validated user input.
        """
        while True:
            user_input = input(prompt)  # Get input from the user
            if input_type == 'name':
                if user_input.strip():  # Check if name is not empty
                    return user_input.strip()  # Return the validated name
                else:
                    print('Name can\'t be empty.')  # Prompt for a valid name
            elif input_type == 'bid':
                try:
                    user_bid = int(user_input)  # Try to convert input to an integer
                    return user_bid  # Return the validated bid
                except ValueError:
                    print('Please enter a valid number.')  # Prompt for a valid number

    def proceed_auction(self):
        """Prompts the user to check if there are more bidders.

        Returns:
            bool: True if there are more bidders, False otherwise.
        """
        while True:
            user_input = input('Are there any other bidders? Type \'yes\' or \'no\': ').lower()
            if user_input == 'yes':
                return True  # Continue the auction
            elif user_input == 'no':
                self.get_winner()  # Determine the winner
                return False  # End the auction
            else:
                print('Please type "yes" or "no".')  # Prompt for valid input

    def get_winner(self):
        """Determines and displays the winner(s) of the auction based on the highest bid."""
        if not self.bids:
            print("No bids were placed.")  # Handle case with no bids
            return

        # Find the maximum bid
        max_bid = max(bid for _, bid in self.bids)
        # Find all winners with the maximum bid
        winners = [user for user, bid in self.bids if bid == max_bid]

        print("Winner(s):")
        for winner in winners:
            print(f"{winner} with a bid of ${max_bid}")  # Display the winner(s) and their bid


def main():
    """Main function to run the Silent Auction."""
    auction = SilentAuction()  # Create an instance of SilentAuction
    auction.start_auction()  # Start the auction


if __name__ == '__main__':
    main()  # Run the main function