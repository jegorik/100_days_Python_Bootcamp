# Day 05 - Password Generator

## Project Description

A secure password generator that creates strong, randomized passwords based on user-specified criteria. This project introduces loops, the random module's advanced features, and practical security concepts while building a real-world utility.

## Learning Objectives

- Working with loops (for loops and iterations)
- Advanced use of the `random` module
- Understanding the `string` module
- List manipulation and shuffling
- Building practical security tools
- User input validation and error handling

## How It Works

The generator prompts users to specify:

1. Number of letters desired in the password
2. Number of symbols to include
3. Number of numbers to include

It then creates a strong password by:

- Randomly selecting characters from each category
- Shuffling all selected characters for maximum security
- Combining them into a final randomized password

## Features

- Customizable password length and composition
- Strong randomization for security
- Multiple character sets (letters, symbols, numbers)
- Password shuffling for enhanced security
- Input validation for all user inputs
- Clean, user-friendly interface

## How to Run

```bash
python password_generator.py
```

## Character Sets Used

- **Letters**: Upper and lowercase (a-z, A-Z)
- **Symbols**: !@#$%^&*()-+=:`~?|;:,"<>[]{}
- **Numbers**: 0-9

## Sample Output

```text
Welcome to Password Generator!
How many letters would you like in your password?
8
How many symbols would you like?
3
How many numbers would you like?
2
Your generated password is: aB7dE!f2@gH#i
```

## Security Features

- **True Randomization**: Uses cryptographically sound random selection
- **Character Shuffling**: Final password is shuffled to prevent patterns
- **Diverse Character Sets**: Includes uppercase, lowercase, symbols, and numbers
- **No Predictable Patterns**: Each password is completely unique

## Code Structure

The generator implements:

- `PasswordGenerator` class with modular design
- Character set initialization using `string` module
- Input validation method for user requirements
- Password generation with random selection
- Shuffling algorithm for enhanced security

## Concepts Learned

- **For Loops**: Iterating specific numbers of times
- **Random Module**: `choices()` and `shuffle()` functions
- **String Module**: Pre-defined character sets
- **List Manipulation**: Extending and shuffling lists
- **Input Validation**: Ensuring positive integer inputs
- **Modular Design**: Breaking complex tasks into methods

## Programming Techniques

- Using `random.choices()` for character selection
- List comprehension and extension methods
- `random.shuffle()` for final randomization
- Exception handling for input validation
- String module constants for character sets

## Security Considerations

This generator follows password security best practices:

- **Length**: Supports variable length passwords
- **Complexity**: Combines multiple character types
- **Randomness**: Uses secure random functions
- **Unpredictability**: Shuffles final result

## Real-World Applications

Password generation is crucial for:

- Account security
- System administration
- Cybersecurity practices
- Application development
- Personal privacy protection

## Possible Enhancements

- Add password strength assessment
- Include custom character sets
- Implement password history tracking
- Add clipboard integration
- Create bulk password generation
- Include pronunciation guides for complex passwords

## Educational Value

This project demonstrates:

- Practical application of randomization
- Security-conscious programming
- Loop usage in real scenarios
- Working with external modules
- Building user-focused utilities

---

*Part of the 100 Days of Python Bootcamp series*
