# Day 04 - Rock Paper Scissors Game

## Project Description

A classic Rock, Paper, Scissors game implemented in Python where players compete against the computer. This project introduces the random module, lists, and more complex game logic while reinforcing conditional statements.

## Learning Objectives

- Working with the `random` module
- Understanding lists and indexing
- Using constants for clean code organization
- Implementing game logic with multiple conditions
- ASCII art for enhanced user experience
- Random number generation and selection

## How It Works

The game follows traditional Rock, Paper, Scissors rules:

- **Rock** crushes **Scissors**
- **Scissors** cuts **Paper**  
- **Paper** covers **Rock**
- Same choices result in a tie

Players input their choice (0=Rock, 1=Paper, 2=Scissors), and the computer makes a random selection.

## Features

- Interactive gameplay against computer AI
- ASCII art representations for each choice
- Clear win/lose/tie logic
- Input validation and error handling
- Random computer opponent
- Visual feedback for both player and computer choices

## How to Run

```bash
python paper_rock_scissors.py
```

## Game Rules

| Player Choice | Computer Choice | Result |
|---------------|-----------------|---------|
| Rock (0) | Scissors (2) | Player Wins |
| Scissors (2) | Paper (1) | Player Wins |
| Paper (1) | Rock (0) | Player Wins |
| Same | Same | Tie |
| All others | - | Computer Wins |

## Sample Output

```text
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
0
You chose:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Computer chose:
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

You win!
```

## Code Structure

The game implements:

- `Game` class with comprehensive game logic
- Constants for Rock, Paper, Scissors choices
- ASCII art dictionary for visual representations
- Methods for game flow and result determination
- Clean separation of display and logic functions

## Concepts Learned

- **Random Module**: Generating random choices for computer opponent
- **Lists**: Storing and accessing choices by index
- **Constants**: Using class constants for magic numbers
- **Dictionaries**: Mapping choices to ASCII art
- **Complex Conditionals**: Multi-condition game logic
- **Code Organization**: Separating concerns into methods

## Programming Techniques

- Random selection with `random.randint()`
- List indexing for choice validation
- Dictionary lookup for ASCII art display
- Nested conditional logic for win/lose determination
- Input validation with range checking

## Game Logic Implementation

The win condition logic efficiently handles all possible combinations:

```python
# Player wins conditions
if (player == 0 and computer == 2) or \
   (player == 1 and computer == 0) or \
   (player == 2 and computer == 1):
    return "You win!"
```

## Educational Value

This project reinforces:

- Logical thinking and condition evaluation
- Working with external modules (random)
- User interface design with ASCII art
- Game development fundamentals
- Code organization and readability

## Possible Enhancements

- Add best-of-three scoring system
- Implement difficulty levels
- Add more choice options (Rock, Paper, Scissors, Lizard, Spock)
- Create multiplayer functionality
- Add game statistics tracking

---

*Part of the 100 Days of Python Bootcamp series*
