# Day 07 - Hangman Game

## Project Description

A classic Hangman word-guessing game where players try to guess a secret word letter by letter before running out of lives. This project introduces functions, lists, string methods, and more complex game logic while creating an engaging interactive experience.

## Learning Objectives

- Defining and calling functions
- Working with lists and string methods
- Implementing game loops and state management
- Using ASCII art for visual feedback
- Creating modular, reusable code
- Managing game state and user progress

## How It Works

The game follows traditional Hangman rules:

1. A random word is selected from a predefined list
2. Players see blanks representing each letter
3. Players guess letters one at a time
4. Correct guesses reveal letter positions
5. Incorrect guesses add to the hangman drawing
6. Players win by guessing the word or lose after 6 wrong guesses

## Features

- Random word selection from extensive word list
- Visual hangman drawing progression
- Letter tracking (guessed letters display)
- Input validation and duplicate guess handling
- ASCII art logo and graphics
- Clear win/lose conditions with feedback

## How to Run

```bash
python hangman_game.py
```

## Game Mechanics

- **Lives**: 6 chances (traditional hangman rules)
- **Word Lists**: Multiple categories of words
- **Letter Tracking**: Shows previously guessed letters
- **Visual Feedback**: ASCII hangman drawing updates with each wrong guess
- **Case Insensitive**: Accepts both upper and lowercase input

## Sample Gameplay

```text
         _                                             
        | |                                            
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
        | '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                            __/ |                      
                           |___/

_ _ _ _ _ _
Guess a letter: a
_ a _ _ _ _
Lives remaining: 6
```

## Code Structure

The game features:

- `Game` class with comprehensive game logic
- ASCII art stored in class dictionaries
- Word lists organized by category
- Methods for each game function (setup, guessing, checking)
- Clean separation of display and logic

## Key Methods

- `start_game()`: Initializes game state and main loop
- `display_current_state()`: Shows word progress and hangman
- `make_guess()`: Handles player input and validation
- `check_guess()`: Evaluates guess against target word
- `update_display()`: Updates visual elements

## Concepts Learned

- **Functions**: Defining reusable code blocks
- **List Methods**: append(), remove(), index()
- **String Methods**: lower(), upper(), replace()
- **Game Loops**: While loops for continuous gameplay
- **State Management**: Tracking game progress
- **ASCII Art**: Enhancing user experience
- **Input Validation**: Handling edge cases

## Programming Techniques

- Random word selection with `random.choice()`
- List comprehension for word display
- String manipulation for letter checking
- Boolean logic for game state evaluation
- Dictionary lookup for ASCII art display

## Game Design Elements

- **Progressive Difficulty**: Visual feedback increases tension
- **Clear Feedback**: Players always know their status
- **Replayability**: Random word selection ensures variety
- **User Experience**: Intuitive interface and clear instructions

## Educational Value

This project reinforces:

- Function design and modularity
- List and string manipulation
- Game loop programming patterns
- User interface design considerations
- Error handling and input validation

## Possible Enhancements

- Add difficulty levels with word categories
- Implement hint system
- Create multiplayer functionality
- Add word definition display
- Include high score tracking
- Create themed word lists
- Add timer challenges

## Real-World Applications

The concepts in this project apply to:

- Game development
- Interactive applications
- User interface design
- Educational software
- Text processing applications

---

*Part of the 100 Days of Python Bootcamp series*
