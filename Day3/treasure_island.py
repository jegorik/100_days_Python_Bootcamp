class Game:
    """
    A class to represent a text-based adventure game where the player navigates through choices
    to find a treasure on an island.
    """

    TREASURE_CHEST = '''
        *******************************************************************************
                  |                   |                  |                     |
         _________|________________.=""_;=.______________|_____________________|_______
        |                   |  ,-"_,=""     '"=.|                  |
        |___________________|__"=._o'"-._        '"=.______________|___________________
                  |                '"=._o'"=._      _'"=._                     |
         _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
        |                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
        |___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
                  |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
         _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
        |                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
        |___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
        ____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
        /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
        ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
        /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
        ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
        /______/______/______/______/______/______/______/______/______/______/_____ /
        *******************************************************************************
        Welcome to Treasure Island.
        Your mission is to find the treasure.
    '''

    GAME_STEPS = {
        'step1': 'You\'re at a cross road. Where do you want to go? Type "left" or "right"\n',
        'step2': 'Type "wait" to wait for a boat. Type "swim" to swim across.\n',
        'step3': 'One red, one yellow and one blue. Which colour do you choose?\n'
    }

    STEP_ACTIONS = {
        'step1': ['left', 'right'],
        'step2': ['swim', 'wait'],
        'step3': ['red', 'yellow', 'blue']
    }

    POSITIVE_CONSEQUENCES = {
        'left': 'You\'ve come to a lake. There is an island in the middle of the lake.',
        'wait': 'You arrive at the island unharmed. There is a house with 3 doors.',
        'yellow': 'You found the treasure! You Win!'
    }

    NEGATIVE_CONSEQUENCES = {
        'right': 'You fell into a hole. Game Over.',
        'swim': 'You get attacked by an angry trout. Game Over.',
        'red': 'It\'s a room full of fire. Game Over.',
        'blue': 'You enter a room of beasts. Game Over.'
    }

    def start_game(self):
        """Starts the game and guides the player through the steps."""
        print(self.TREASURE_CHEST)
        player_choice = None

        for step in self.GAME_STEPS:
            # Print positive consequences from previous choices
            if player_choice is not None:
                print(self.POSITIVE_CONSEQUENCES.get(player_choice, ''))
            # Get player's choice for the current step
            player_choice = self.get_player_input(self.GAME_STEPS[step], self.STEP_ACTIONS[step])

            # Check if the choice leads to game over
            if player_choice in self.NEGATIVE_CONSEQUENCES or player_choice == 'yellow':
                self.game_over(player_choice)

    def get_player_input(self, prompt, actions):
        """Prompts the player for input until a valid action is chosen."""
        while True:
            player_input = input(prompt).lower()  # Normalize input to lowercase
            if player_input in actions:
                return player_input
            else:
                print(f'Please choose from: ' + ' or '.join(actions))

    def game_over(self, player_choice):
        """Handles the game over scenario based on the player's choice."""
        if player_choice == 'yellow':
            print(self.POSITIVE_CONSEQUENCES[player_choice])
        else:
            print(self.NEGATIVE_CONSEQUENCES[player_choice])
        exit()


def main():
    """Main function to start the game."""
    game = Game()
    game.start_game()


if __name__ == '__main__':
    main()