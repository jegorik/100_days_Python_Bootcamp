# Day 11 - Blackjack Game

## Project Description

A complete implementation of the classic Blackjack (21) card game where players compete against the dealer. This project combines lists, functions, game logic, and probability concepts to create an engaging casino-style card game.

## Learning Objectives

- Complex list manipulation and management
- Advanced function design and organization
- Game state management and logic
- Probability and random selection concepts
- Rule-based programming
- Interactive game development

## How It Works

The game follows standard Blackjack rules:

1. Player and dealer each receive 2 initial cards
2. Player can "hit" (take more cards) or "stand" (keep current hand)
3. Goal is to get as close to 21 as possible without going over
4. Dealer must hit if total is under 17
5. Aces count as 1 or 11 (whichever is better)
6. Face cards (J, Q, K) count as 10

## Game Rules

- **Blackjack**: 21 with first 2 cards (Ace + 10-value card)
- **Bust**: Total exceeds 21 (automatic loss)
- **Dealer Rules**: Must hit on 16, stand on 17
- **Ace Handling**: Automatically adjusts between 1 and 11
- **Win Conditions**: Higher total without busting, or dealer busts

## Features

- Complete Blackjack rule implementation
- Smart Ace value calculation
- Interactive player decisions
- Dealer AI following casino rules
- Clear game status display
- ASCII art logo and card representations
- Multiple game rounds support

## How to Run

```bash
python blackjack.py
```

## Sample Gameplay

```text
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/     

Your cards: [11, 10], current score: 21
Computer's first card: 7
Do you want to draw another card? Type 'y' or 'n': n
Your final hand: [11, 10], final score: 21
Computer's final hand: [7, 6, 9], final score: 22
Opponent went over. You win 😃
```

## Code Structure

The game implements:

- `BlackjackGame` class managing all game logic
- Card dealing and hand management systems
- Score calculation with Ace adjustment
- Win/lose condition evaluation
- Player and dealer decision logic

## Key Methods

- `deal_card()`: Random card selection from deck
- `calculate_score()`: Smart score calculation with Ace handling
- `compare()`: Determine winner based on final scores
- `play_game()`: Main game loop and flow control

## Card Values

```python
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
```

- **Ace**: 11 (automatically becomes 1 if needed)
- **Number Cards**: Face value (2-10)
- **Face Cards**: All worth 10 points

## Concepts Learned

- **List Operations**: Managing dynamic card collections
- **Complex Logic**: Multiple winning/losing conditions
- **State Management**: Tracking game progress
- **Random Selection**: Simulating card drawing
- **Conditional Logic**: Rule-based decision making
- **Game Flow Design**: Turn-based interaction patterns

## Programming Techniques

- Dynamic list modification with append()
- Conditional value adjustment for Aces
- Complex boolean logic for win conditions
- Random selection with replacement
- Interactive input handling
- Game state evaluation

## Game Logic Implementation

The score calculation handles Ace values intelligently:

```python
def calculate_score(cards):
    score = sum(cards)
    # Convert Ace from 11 to 1 if score > 21
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score
```

## Win Conditions

- **Player Blackjack**: 21 with 2 cards
- **Player Wins**: Higher score without busting
- **Dealer Busts**: Dealer exceeds 21
- **Dealer Wins**: Higher score or player busts
- **Draw**: Equal scores

## Educational Value

This project reinforces:

- Complex conditional logic
- List manipulation techniques
- Game design principles
- Probability concepts
- User interface design
- Rule-based programming

## Real-World Applications

Blackjack concepts apply to:

- Casino game development
- Card game applications
- Probability simulations
- Decision-making algorithms
- Interactive entertainment software

## Possible Enhancements

- Add betting system with chips
- Implement card counting features
- Create multiple deck support
- Add split and double down options
- Include insurance betting
- Build multiplayer functionality
- Add statistics tracking

## Probability Concepts

The game demonstrates:

- **Random Distribution**: Card drawing probability
- **Risk Assessment**: Hit vs. stand decisions
- **Expected Value**: Optimal strategy concepts
- **Statistical Outcomes**: Win/loss ratios

## Strategy Elements

Players learn to consider:

- Current hand value
- Dealer's visible card
- Probability of busting
- Optimal hit/stand decisions
- Risk vs. reward calculations

---

*Part of the 100 Days of Python Bootcamp series*
