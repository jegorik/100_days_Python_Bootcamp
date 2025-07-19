# Day 12 - Guess the Number Game

## Project Description

A number guessing game where players try to guess a randomly selected number within a limited number of attempts. This project explores scope concepts, global vs local variables, and difficulty-based game mechanics.

## Learning Objectives

- Understanding scope and variable accessibility
- Global vs local variable concepts
- Difficulty level implementation
- Game balance and player experience
- Random number generation within ranges
- Attempt tracking and management

## How It Works

The game mechanics:

1. Computer randomly selects a number between 1 and 100
2. Player chooses difficulty level (Easy: 10 attempts, Hard: 5 attempts)
3. Player makes guesses and receives "too high" or "too low" feedback
4. Game ends when number is guessed correctly or attempts run out
5. Player can play multiple rounds

## Difficulty Levels

- **Easy Mode**: 10 attempts to guess the number
- **Hard Mode**: 5 attempts to guess the number
- **Feedback System**: Directional hints for each guess
- **Attempt Tracking**: Clear display of remaining chances

## Features

- Two difficulty levels for varied challenge
- Clear feedback system for each guess
- Attempt counter with remaining chances
- Input validation for guesses and difficulty selection
- Replay functionality for multiple rounds
- ASCII art logo and engaging interface

## How to Run

```bash
python guess_number.py
```

## Sample Gameplay
 ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba,  
a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    ""  
8b       88 88       88 8PP"""""""  `"Y8ba,   `"Y8ba,   
"8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I  
 `"YbbdP"Y8  `"YbbdP'Y8  `"Ybbd8"' `"YbbdP"' `"YbbdP"'  
 aa,    ,88                                             
  "Y8bbdP"   
```text
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __   
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|  
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|                                                

Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Choose a difficulty. Type 'easy' or 'hard': easy
You have 10 attempts remaining to guess the number.
Make a guess: 50
Too high.
Guess again.
You have 9 attempts remaining to guess the number.
Make a guess: 25
Too low.
Guess again.
You have 8 attempts remaining to guess the number.
Make a guess: 37
You got it! The answer was 37.
```

## Code Structure

The game implements:

- `GuessTheNumber` class with game management
- Difficulty level configuration
- Scope management for attempts and target number
- Input validation and feedback systems
- Game state tracking

## Key Methods

- `set_difficulty()`: Configure attempts based on difficulty
- `make_guess()`: Handle player input and provide feedback
- `check_guess()`: Compare guess with target number
- `play_game()`: Main game loop and flow control

## Scope Concepts Demonstrated

```python
class GuessTheNumber:
    def __init__(self):
        self.number = random.randint(1, 100)  # Instance variable
        self.attempts = 0  # Instance variable
    
    def play_game(self):
        difficulty = input("Choose difficulty: ")  # Local variable
        self.attempts = self.set_difficulty(difficulty)  # Global scope
```

## Concepts Learned

- **Variable Scope**: Local vs instance vs global variables
- **State Management**: Tracking game progress across methods
- **Difficulty Scaling**: Adjusting game parameters
- **User Feedback**: Providing helpful guidance
- **Game Balance**: Creating appropriate challenge levels
- **Input Validation**: Ensuring valid user input

## Programming Techniques

- Instance variable management for game state
- Method parameter passing for configuration
- Conditional logic for difficulty settings
- Range validation for number guessing
- Loop control for attempt management
- Boolean flags for game completion

## Game Design Elements

- **Progressive Feedback**: Directional hints improve player experience
- **Difficulty Options**: Accommodates different skill levels
- **Clear Communication**: Transparent attempt tracking
- **Immediate Feedback**: Instant response to each guess
- **Replay Value**: Multiple rounds with different numbers

## Educational Value

This project teaches:

- Scope and variable lifecycle concepts
- Game state management techniques
- User experience design principles
- Random number generation applications
- Input validation best practices

## Scope Examples

The game demonstrates different scope levels:

- **Local Scope**: Variables within method functions
- **Instance Scope**: Variables shared across class methods
- **Method Scope**: Parameters passed between functions
- **Conditional Scope**: Variables within if/else blocks

## Real-World Applications

Number guessing concepts apply to:

- Game development and balancing
- Binary search algorithms
- User interface design
- Educational software
- Statistical simulations

## Possible Enhancements

- Add scoring system based on attempts used
- Implement hint system for struggling players
- Create themed variations (guess the year, price, etc.)
- Add multiplayer competition mode
- Include statistics tracking across games
- Build custom number ranges
- Add time pressure elements

## Algorithm Concepts

The game introduces:

- **Linear Search**: Player's guessing strategy
- **Binary Search**: Optimal guessing strategy
- **Random Generation**: Fair number selection
- **State Machines**: Game flow management
- **Feedback Loops**: Player guidance systems

## Strategy Tips for Players

- **Binary Search Approach**: Start with 50, then narrow range
- **Range Management**: Keep track of high/low bounds
- **Attempt Conservation**: Think before guessing in hard mode
- **Pattern Recognition**: Learn from previous games

---

*Part of the 100 Days of Python Bootcamp series*
