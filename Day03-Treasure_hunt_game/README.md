# Day 03 - Treasure Island Game

## Project Description

An interactive text-based adventure game where players navigate through a series of choices to find treasure on a mysterious island. This project introduces conditional statements, logical operators, and control flow in Python.

## Learning Objectives

- Understanding conditional statements (if, elif, else)
- Working with logical operators (and, or, not)
- Implementing control flow and decision trees
- Creating interactive storylines
- ASCII art integration
- Game logic and user experience design

## How It Works

Players make a series of choices that determine their fate:

1. **Direction Choice**: Left or Right at the crossroad
2. **Action Choice**: Wait or Swim at the lake
3. **Door Choice**: Red, Blue, or Yellow door at the house

Only one specific combination of choices leads to finding the treasure!

## Features

- Interactive story-driven gameplay
- Multiple decision points and branching paths
- ASCII art for visual enhancement
- Clear win/lose conditions
- Engaging narrative elements
- Object-oriented game structure

## How to Run

```bash
python treasure_island.py
```

## Game Flow

```text
Start → Crossroad → Lake → House → Outcome
         (L/R)     (W/S)   (R/B/Y)
```

## Winning Path

**Spoiler Alert**: The winning combination is Left → Wait → Yellow

## Sample Output

```text
Welcome to Treasure Island.
Your mission is to find the treasure.
You're at a crossroad. Where do you want to go? Type "left" or "right"
left
You've come to a lake. There is an island in the middle of the lake...
[Game continues based on choices]
```

## Code Structure

The game uses:

- `Game` class to encapsulate all game logic
- ASCII art stored as class constants
- Methods for each decision point
- Clear separation of story elements and logic
- Comprehensive error handling

## Concepts Learned

- **Conditional Statements**: if/elif/else chains
- **String Comparison**: Case-insensitive input handling
- **Logical Flow**: Creating branching narratives
- **Code Organization**: Separating concerns in methods
- **User Input Validation**: Handling unexpected inputs
- **ASCII Art**: Enhancing user experience with visuals

## Game Design Elements

- **Narrative Structure**: Beginning, middle, and multiple endings
- **Player Agency**: Meaningful choices that affect outcomes
- **Feedback Systems**: Clear consequences for each decision
- **Visual Elements**: ASCII art to enhance immersion

## Programming Techniques

- Nested conditional statements
- String methods for input processing
- Class-based organization
- Constants for reusable content
- Method chaining for game flow

## Educational Value

This project demonstrates:

- Problem decomposition into smaller decisions
- Boolean logic in practical applications
- User interface design considerations
- Story-driven programming concepts

## Possible Enhancements

- Add more paths and endings
- Implement a scoring system
- Create save/load functionality
- Add random elements for replayability
- Include inventory management

---

*Part of the 100 Days of Python Bootcamp series*
