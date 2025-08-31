# Day 14 - Higher Lower Game

## Project Overview

The Higher Lower Game is an interactive guessing game where players compare the follower counts of celebrities, influencers, and popular entities. Players must guess which option has more followers on social media platforms.

## How to Play

1. The game presents two options (A and B) with their names, descriptions, and countries
2. You need to guess which one has more followers
3. Enter 'A' or 'B' to make your choice
4. Get points for correct guesses
5. The game ends when you make an incorrect guess
6. Try to achieve the highest score possible!

## Features

- **Object-Oriented Design**: Clean class-based implementation
- **Type Hints**: Enhanced code readability and IDE support
- **Error Handling**: Robust input validation and exception handling
- **Rich Data Set**: Wide variety of celebrities and entities to compare
- **Score Tracking**: Keep track of your consecutive correct guesses
- **ASCII Art**: Eye-catching game logo and visual elements

## Files Structure

```text
Day14-HigherLowerGame/
├── higher_or_lower.py    # Main game logic and HigherLower class
├── game_data.py          # Database of celebrities/entities with follower counts
├── art.py                # ASCII art for logo and visual elements
└── README.md             # This file
```

## Code Concepts Demonstrated

- **Classes and Objects**: Game logic encapsulated in a HigherLower class
- **Method Organization**: Logical separation of game functionality
- **Type Hints**: Professional Python development practices
- **Error Handling**: Graceful handling of edge cases and user input
- **Data Validation**: Ensuring game data integrity
- **Random Selection**: Using Python's random module for game mechanics
- **Input Validation**: Robust user input handling with retry logic
- **Game State Management**: Tracking score and game status

## How to Run

```bash
python higher_or_lower.py
```

## Game Data

The game includes data for various celebrities and entities including:

- Social media platforms (Instagram, TikTok, etc.)
- Musicians and artists
- Athletes and sports figures
- Actors and celebrities
- Public figures and influencers

Each entry contains:

- Name
- Follower count (in millions)
- Description/profession
- Country of origin

## Learning Objectives

Through this project, you'll practice:

1. **Object-Oriented Programming**: Creating and using classes effectively
2. **Error Handling**: Implementing try-catch blocks and validation
3. **Type Hints**: Writing more maintainable and readable code
4. **Game Logic**: Implementing turn-based game mechanics
5. **Data Management**: Working with structured data and dictionaries
6. **User Experience**: Creating engaging interactive applications

## Sample Gameplay

```text
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     

Welcome to the Higher Lower Game!

Compare A: Instagram, a Social media platform, from United States
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

Against B: Cristiano Ronaldo, a Footballer, from Portugal
Who has more followers? Type 'A' or 'B': a

You're right! Current score: 1
The answer was 346 million followers.
```

## Possible Enhancements

- Add difficulty levels with different data sets
- Implement a leaderboard system
- Add more detailed statistics after each game
- Create a web interface version
- Add sound effects and animations
- Include trending topics and real-time data updates

---

*This project demonstrates intermediate Python programming concepts including OOP, error handling, and game development principles.*

*Part of the 100 Days of Python Bootcamp series*