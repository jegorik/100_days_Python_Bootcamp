# Day 01 - Band Name Generator

## Project Description

A simple Python program that generates a band name by combining the user's hometown and pet's name. This project introduces basic Python concepts like variables, user input, and string manipulation.

## Learning Objectives

- Understanding variables and string concatenation
- Working with user input using `input()` function
- Basic string formatting with f-strings
- Introduction to Python classes and methods
- Print statements and output formatting

## How It Works

The program prompts the user for two pieces of information:

1. The name of the city they grew up in
2. Their pet's name

It then combines these two inputs to create a unique band name suggestion.

## Features

- Interactive user input
- Clean, formatted output
- Object-oriented design with a `BandNameGenerator` class
- Simple and beginner-friendly code structure

## How to Run

```bash
python band_name_generator.py
```

## Sample Output

```text
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
New York
What's your pet's name?
Buddy
Your band name could be New York Buddy
```

## Code Structure

The program uses a class-based approach:

- `BandNameGenerator` class handles the main functionality
- `__init__` method provides a welcome message
- `name_generation` method handles input collection and name creation
- `main` function orchestrates the program execution

## Concepts Learned

- **Variables**: Storing user input in variables
- **String Interpolation**: Using f-strings for formatted output
- **User Input**: Collecting data from users with `input()`
- **Classes**: Basic object-oriented programming structure
- **Methods**: Organizing code into reusable functions

## Next Steps

This foundational project sets the stage for more complex programs involving:

- Data validation
- Error handling
- More sophisticated string manipulation
- Enhanced user interaction

---

*Part of the 100 Days of Python Bootcamp series*
