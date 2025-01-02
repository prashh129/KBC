# Quiz Game

This repository contains a simple console-based quiz game written in Python. The game presents a series of multiple-choice questions, and the player earns money for every correct answer. The game ends when the player either answers a question incorrectly or completes all the questions.

## How It Works

1. The game consists of a list of 10 questions, each with four answer choices.
2. Each question has a specific prize amount, as defined in the `levels` list.
3. Players input their answers by typing `a`, `b`, `c`, or `d`.
4. If the player's answer matches the correct answer, they win the corresponding prize amount and proceed to the next question.
5. If the player answers incorrectly, the game ends, and they take home the amount won at the last milestone.

## Milestones

- **Question 5**: If you answer the fifth question correctly, you are guaranteed to take home Rs. 10,000.
- **Question 10**: Completing all questions guarantees a total prize of Rs. 320,000.

## Game Logic

- The `questions` list contains each question, its answer choices, and the correct answer index.
- The `levels` list defines the prize amounts for each question.
- The player's progress is tracked, and the game ends when the player provides an incorrect answer.

## Sample Question Format

```
Which programming language is used in Facebook?

a. Python            b. PHP
c. Javascript        d. Nepali
Enter your answer (a-d):
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/prashh129/KBC.git
   cd KBC
   ```

2. Run the Python script:
   ```bash
   python quiz_game.py
   ```

## Requirements

- Python 3.x installed on your system.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Suggestions for improvements, additional features, or bug fixes are welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

Thanks for checking out this project! If you have any feedback or questions, please feel free to open an issue or contact me directly.
