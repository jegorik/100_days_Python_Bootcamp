from random import shuffle
from enum import Enum


class Action(Enum):
    """Enumeration for player actions in the game."""
    HIT = 'hit'
    STAY = 'stay'


class Card:
    """Represents a playing card with a suit, rank, and value."""

    def __init__(self, suit: str, rank: str, value: int):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    """Represents a deck of cards for the game."""

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
              'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

    def __init__(self):
        """Initializes a new deck and shuffles it."""
        self.deck = []
        self.create_deck()

    def create_deck(self):
        """Creates a standard deck of 52 cards and shuffles it."""
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank, self.values[rank]))
        shuffle(self.deck)


class Player:
    """Represents a player in the game, including their stake and cards on hand."""

    def __init__(self):
        self.stake = 0
        self.account = 1000  # Starting account balance
        self.cards_on_hand = []

    def reset_hand(self):
        """Resets the player's hand for a new game."""
        self.cards_on_hand = []


class Bank:
    """Represents the bank that holds the current stake for the game."""

    def __init__(self):
        self.stake = 0  # Current stake in the game


class Game:
    """Main class to manage the Blackjack game logic."""

    BLACKJACK = 21  # Constant for the winning score in Blackjack

    def __init__(self):
        """Initializes a new game instance with a deck, player, dealer, and bank."""
        self.game_deck = Deck()
        self.player = Player()
        self.dealer = Player()
        self.bank = Bank()

    def new_game(self):
        """Starts a new game loop until the player chooses to stop or runs out of money."""
        while True:
            self.game_deck = Deck()
            self.player.reset_hand()
            self.dealer.reset_hand()
            self.bank.stake = 0
            self.make_stake()
            self.deal_cards(2, self.player)
            self.deal_cards(2, self.dealer)
            self.game_status()
            if self.player.account <= 0:
                print("You don't have enough money to continue playing. Game over!")
                break
            if not self.play_again():
                break

    def make_stake(self):
        """Prompts the player to make a stake for the current round."""
        player_stake = self.validate_stake_input(f'Account: {self.player.account} Please make stake: ')
        self.player.account -= player_stake
        self.bank.stake = player_stake

    def deal_cards(self, number_of_cards: int, player: Player):
        """Deals a specified number of cards to the given player."""
        for _ in range(number_of_cards):
            player.cards_on_hand.append(self.game_deck.deck.pop())

    def game_status(self):
        """Manages the game status and player actions during a round."""
        while True:
            player_sum = self.get_cards_sum(self.player.cards_on_hand)
            dealer_sum = self.get_cards_sum(self.dealer.cards_on_hand)
            self.print_table()

            if self.check_win_conditions(player_sum, dealer_sum):
                break

            player_action = self.validate_hit_stay_input('Please choose "Hit" or "Stay": ')
            if player_action == Action.STAY.value:
                if dealer_sum > player_sum:
                    print('Dealer Wins!')
                    break
                else:
                    self.dealer_play(player_sum)  # Dealer plays after player stays
                    self.determine_winner(player_sum, self.get_cards_sum(self.dealer.cards_on_hand))
                    break
            elif player_action == Action.HIT.value:
                self.deal_cards(1, self.player)

    def check_win_conditions(self, player_sum: int, dealer_sum: int) -> bool:
        """Checks the win conditions and updates the player's account accordingly."""
        if player_sum == self.BLACKJACK and dealer_sum == self.BLACKJACK:
            self.player.account += self.bank.stake
            print('It\'s a Draw!')
        elif player_sum == self.BLACKJACK:
            print('Player has 21. Player Wins!')
            self.player.account += self.bank.stake * 2
            return True
        elif dealer_sum == self.BLACKJACK:
            print('Dealer has 21. Dealer Wins!')
            return True
        elif player_sum > self.BLACKJACK:
            print('Player busted!')
            return True
        elif dealer_sum > self.BLACKJACK:
            print('Dealer busted! Player Wins!')
            self.player.account += self.bank.stake * 2
            return True
        return False

    def dealer_play(self, player_sum):
        """Handles the dealer's actions according to the game rules."""
        dealer_sum = self.get_cards_sum(self.dealer.cards_on_hand)
        while dealer_sum < self.BLACKJACK and (dealer_sum < player_sum or dealer_sum == player_sum):
            self.deal_cards(1, self.dealer)
            dealer_sum = self.get_cards_sum(self.dealer.cards_on_hand)

    def determine_winner(self, player_sum: int, dealer_sum: int):
        """Determines the winner of the round and updates the player's account."""
        self.print_table()
        if dealer_sum > self.BLACKJACK or player_sum > dealer_sum:
            print('Player Wins!')
            self.player.account += self.bank.stake * 2
        elif player_sum < dealer_sum:
            print('Dealer Wins!')
        else:
            self.player.account += self.bank.stake
            print('It\'s a Draw!')

    def get_cards_sum(self, cards_on_hand: list[Card]) -> int:
        """Calculates the total value of the cards in hand."""
        return sum(card.value for card in cards_on_hand)

    def validate_stake_input(self, prompt: str) -> int:
        """Validates the player's stake input and ensures it's a valid number."""
        while True:
            try:
                player_input = int(input(prompt))
                if self.check_player_stake(player_input):
                    return player_input
                else:
                    print('Not enough money to make stake.')
            except ValueError:
                print('Input numbers only.')

    def validate_hit_stay_input(self, prompt: str) -> str:
        """Validates the player's choice to hit or stay."""
        while True:
            player_input = input(prompt).lower()
            if player_input in [action.value for action in Action]:
                return player_input
            else:
                print('Choose "Hit" or "Stay".')

    def check_player_stake(self, player_input: int) -> bool:
        """Checks if the player's stake is valid based on their account balance."""
        if self.player.account >= player_input > 0:
            self.player.stake = player_input
            return True
        return False

    def print_table(self):
        """Prints the current game status, including player and dealer cards and account balance."""
        print(f'Account: {self.player.account} Game Bank: {self.bank.stake}')
        print(f'Player cards: {", ".join(str(card) for card in self.player.cards_on_hand)} [Total: {self.get_cards_sum(self.player.cards_on_hand)}]')
        print(f'Dealer cards: {", ".join(str(card) for card in self.dealer.cards_on_hand)} [Total: {self.get_cards_sum(self.dealer.cards_on_hand)}]')

    def play_again(self) -> bool:
        """Prompts the player to decide whether to play again."""
        while True:
            player_input = input('Do you want to play again? (yes/no): ').lower()
            if player_input in ['yes', 'no']:
                return True if player_input == 'yes' else False
            else:
                print('Write \'yes\' or \'no\'')



def main():
    """Main function to start the Blackjack game."""
    game = Game()
    game.new_game()


if __name__ == '__main__':
    main()