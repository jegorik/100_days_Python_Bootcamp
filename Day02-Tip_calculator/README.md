# Day 02 - Tip Calculator

## Project Description

A practical tip calculator that helps users determine how much each person should pay when splitting a bill with tips. This project builds on Day 1 concepts while introducing mathematical operations, data types, and input validation.

## Learning Objectives

- Working with different data types (int, float, string)
- Type conversion and casting
- Mathematical operations and calculations
- Input validation and error handling
- Rounding numbers for currency display
- Creating user-friendly interfaces

## How It Works

The calculator prompts users for:

1. Total bill amount
2. Tip percentage they want to give
3. Number of people splitting the bill

It then calculates the amount each person should pay, including the tip.

## Features

- Input validation for positive numbers
- Handles decimal calculations accurately
- Rounds final amount to 2 decimal places
- Clear, formatted output
- Error handling for invalid inputs
- Object-oriented design

## How to Run

```bash
python tip_calculator.py
```

## Sample Output

```text
Welcome to the tip calculator!
What was the total bill? $150.00
How much tip would you like to give? (in percentage): 18
How many people to split the bill? 4
Each person should pay: $44.25
```

## Code Structure

The program features:

- `TipCalculator` class with comprehensive documentation
- Input validation method `get_positive_input()`
- Calculation logic in `calculate_tip_per_person()`
- Proper error handling and user feedback
- Clean separation of concerns

## Mathematical Logic

```text
Total with tip = Bill × (1 + Tip% ÷ 100)
Amount per person = Total with tip ÷ Number of people
```

## Concepts Learned

- **Data Types**: Understanding int, float, and string types
- **Type Conversion**: Converting string input to numbers
- **Mathematical Operations**: Addition, multiplication, division
- **Rounding**: Using round() function for currency formatting
- **Input Validation**: Ensuring user provides valid data
- **Error Handling**: Managing invalid input gracefully
- **Documentation**: Writing clear docstrings and comments

## Key Programming Techniques

- Exception handling with try-except blocks
- While loops for input validation
- Method organization and single responsibility principle
- User experience considerations in program flow

## Real-World Application

This calculator demonstrates practical programming by solving a common real-world problem. The concepts learned here apply to:

- Financial applications
- E-commerce systems
- Point-of-sale software
- Budgeting tools

---

*Part of the 100 Days of Python Bootcamp series*
