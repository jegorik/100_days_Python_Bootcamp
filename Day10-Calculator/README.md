# Day 10 - Calculator

## Project Description

A fully functional calculator application that performs basic arithmetic operations with a clean interface and continuous calculation capability. This project focuses on functions with outputs, recursion, and building a practical computational tool.

## Learning Objectives

- Functions with return values and outputs
- Understanding recursion and function calls
- Building modular, reusable code
- Dictionary-based operation mapping
- Error handling and input validation
- Creating user-friendly interfaces

## How It Works

The calculator provides:

1. Basic arithmetic operations (+, -, *, /)
2. Continuous calculation capability
3. Option to start fresh or continue with previous result
4. Input validation and error handling
5. Clear operation feedback and results

## Features

- Four basic arithmetic operations
- Continuous calculation mode
- Result memory for chained operations
- Input validation for numbers and operations
- Division by zero error handling
- Clean, intuitive user interface
- ASCII art logo

## How to Run

```bash
python calculator.py
```

## Supported Operations

| Symbol | Operation | Example |
|--------|-----------|---------|
| + | Addition | 5 + 3 = 8 |
| - | Subtraction | 10 - 4 = 6 |
| * | Multiplication | 7 * 2 = 14 |
| / | Division | 15 / 3 = 5 |

## Sample Usage

```text
 _____________________
|  _________________  |
| | Pythonista   0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

What's the first number?: 10
Pick an operation: +
What's the next number?: 5
10.0 + 5.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: y
Pick an operation: *
What's the next number?: 2
15.0 * 2.0 = 30.0
```

## Code Structure

The calculator implements:

- `Calculator` class with operation methods
- Dictionary mapping symbols to functions
- Recursive calculation flow
- Input validation and error handling
- Clean separation of concerns

## Key Methods

- `add()`, `subtract()`, `multiply()`, `divide()`: Basic operations
- `calculate()`: Main calculation logic
- `run()`: Program flow control and user interface
- Input validation methods for numbers and operations

## Mathematical Operations

```python
operations = {
    "+": self.add,
    "-": self.subtract,
    "*": self.multiply,
    "/": self.divide,
}
```

## Concepts Learned

- **Functions with Outputs**: Using return statements effectively
- **Recursion**: Functions calling themselves for program flow
- **Dictionary Mapping**: Associating symbols with functions
- **Error Handling**: Managing division by zero and invalid inputs
- **Program State**: Maintaining calculation history
- **User Experience**: Designing intuitive interfaces

## Programming Techniques

- Function definition and calling
- Dictionary-based dispatch patterns
- Exception handling with try-catch blocks
- Input validation and sanitization
- Recursive program flow design
- Boolean logic for continuation control

## Error Handling

The calculator handles:

- **Division by Zero**: Prevents crashes with appropriate error messages
- **Invalid Operations**: Validates operation symbols
- **Non-numeric Input**: Ensures numeric values for calculations
- **Empty Input**: Handles missing or invalid entries

## Educational Value

This project demonstrates:

- Function design and modularity
- Mathematical operation implementation
- User interface design principles
- Error handling best practices
- Program flow control with recursion

## Real-World Applications

Calculator concepts apply to:

- Financial applications
- Scientific computing tools
- Engineering calculators
- Educational software
- Mobile calculator apps

## Possible Enhancements

- Add advanced mathematical functions (sin, cos, sqrt, etc.)
- Implement memory storage and recall
- Create expression parsing for complex equations
- Add scientific notation support
- Include calculation history
- Build graphical user interface
- Add unit conversion capabilities

## Design Patterns

The calculator demonstrates:

- **Strategy Pattern**: Different operations via dictionary dispatch
- **Command Pattern**: Operations as callable functions
- **State Management**: Maintaining current calculation value
- **Input Validation**: Ensuring data integrity

## Testing Considerations

Key test cases include:

- Basic arithmetic accuracy
- Division by zero handling
- Invalid input management
- Continuous calculation flow
- Edge cases with very large/small numbers

---

*Part of the 100 Days of Python Bootcamp series*
