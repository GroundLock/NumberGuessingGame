# Number Guessing Game
https://roadmap.sh/projects/number-guessing-game

A simple Python program where you try to guess a randomly selected number between 1 and 100. The game offers multiple difficulty levels to suit your challenge preference.

## Features
- Randomly generates a number between 1 and 100.
- Offers three difficulty levels:
  - Easy: 10 attempts
  - Medium: 5 attempts
  - Hard: 3 attempts
- Provides hints after each incorrect guess, indicating whether the number is higher or lower than your guess.
- Keeps track of the number of attempts used.

## How to Run
1. Make sure you have Python installed on your computer (version 3.x recommended).
2. Copy the code from [number_guessing_game.py](number_guessing_game.py) into a file.
3. Open a terminal and navigate to the directory containing the file.
4. Run the program by typing:
   ```bash
   python number_guessing_game.py
   ```

## Gameplay Instructions
1. The program will prompt you to choose a difficulty level:
   - 1 for Easy (10 chances)
   - 2 for Medium (5 chances)
   - 3 for Hard (3 chances)
2. Enter your difficulty choice.
3. Guess the number by typing your guess and pressing Enter.
4. The program will provide feedback on whether the number is higher or lower than your guess.
5. Continue guessing until you find the correct number or run out of attempts.

## Example
```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: 
>1
Great! You have selected the Easy difficulty level.

Enter your guess: 
>50
Incorrect! The number is greater than 50.

Enter your guess: 
>75
Congratulations! You guessed the correct number in 2 attempts.
```

## Dependencies
This program uses Python's built-in libraries and requires no additional dependencies.

## License
This project is released under the MIT License.

Feel free to modify and enhance the program as you like!
