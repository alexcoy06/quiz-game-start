# Quiz Game (OOP-Based)

## Overview
This is a simple Quiz Game built using Python and Object-Oriented Programming (OOP) concepts. The project was developed as part of a challenge by Dr. Angela Yu to practice working with classes and reusability in Python.

The game runs in the console. It focuses on structuring code using OOP principles to make the quiz logic modular and extendable.

## Features
- Utilizes OOP for better code organization and reusability.
- Retrieves quiz questions dynamically from a dataset.
- Implements a QuizBrain class to manage game logic.
- Supports multiple-choice or true/false questions.
- Provides real-time feedback on correct and incorrect answers.
- Displays final scores at the end of the quiz.

## Technologies Used
- Python 3
- OOP (Classes & Objects)
- File Handling 
- Random module 

## How to Run
1. Clone this repository (or download the files manually):
   ```sh
   git clone https://github.com/yourusername/quiz-game.git
   cd quiz-game
   ```
2. Run the script:
   ```sh
   python main.py
   ```

## Project Structure
```
quiz-game/
│── main.py           # Entry point for the game
│── question_model.py # Defines Question class
│── quiz_brain.py     # Handles quiz logic
│── data.py           # Stores questions (or fetches from an API)
│── README.md         # Project documentation
```

## How It Works
1. The Question class (in `question_model.py`) represents each quiz question.
2. The QuizBrain class (in `quiz_brain.py`) manages the quiz flow, tracks scores, and checks answers.
3. The `data.py` file contains a list of questions and answers.
4. The `main.py` file initializes the quiz and runs the game loop.

## Lessons Learned
- Encapsulation: Organized logic into separate classes.
- Reusability: Designed modular code that can be extended for new features (e.g., GUI, API-based questions).
- OOP Principles: Practiced abstraction, inheritance, and method structuring.

## Future Improvements
- Add a GUI version.
- Fetch questions from an API.
- Implement difficulty levels or timed quizzes.
