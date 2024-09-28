# Number Guessing Game

This repository contains two versions of a simple Python-based Number Guessing Game:
1. **Command-Line Version**: A basic version of the game that runs in the terminal.
2. **GUI Version**: A more interactive version built using the `tkinter` library to provide a graphical user interface.

## Features
### Command-Line Version:
- The player guesses a number between 1 and 100.
- Feedback is provided for each guess (higher/lower).
- The number of guesses is tracked and displayed when the player guesses correctly.
- The game can be exited by entering 'e'.

### GUI Version (Tkinter):
- A user-friendly interface with color-coded feedback.
- Feedback for each guess (higher/lower) is displayed visually in the app window.
- A counter that tracks the number of guesses made.
- The game resets automatically after a correct guess, allowing continuous gameplay.
- Input validation to handle invalid entries (non-numeric input).
- Attractive and modern design using `tkinter`.

---

## Demo

### Command-Line Version:
In the command-line version, the player is prompted to guess a number between 1 and 100. The game responds with "Higher" or "Lower" until the correct number is guessed.

### GUI Version:
The GUI version offers a simple window where users can enter their guesses and receive immediate feedback. Correct guesses trigger a message box, and the game resets for another round.

---

## Screenshots

![GUI Version Screenshot](path_to_screenshot_image) <!-- You can add a screenshot of the tkinter version here -->

---

## Installation and Usage

### 1. Command-Line Version

To run the command-line version of the game:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/number-guessing-game.git
    cd number-guessing-game
    ```

2. **Run the game**:
    ```bash
    python number_guess_cli.py
    ```

### 2. GUI Version (Tkinter)

To run the `tkinter` version of the game:

1. **Ensure you have Python 3 installed**.

2. **Install Tkinter** (if not already installed):
   - For **Linux**: `sudo apt-get install python3-tk`
   - For **Mac**: Tkinter is usually included with Python installations.
   - For **Windows**: Tkinter comes pre-installed with Python.

3. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/number-guessing-game.git
    cd number-guessing-game
    ```

4. **Run the game**:
    ```bash
    python number_guess_gui.py
    ```

---

## How to Play

### Command-Line Version:
1. Run the game.
2. The game will prompt you to guess a number between 1 and 100.
3. Enter your guess and press Enter.
4. If your guess is too low, the game will display "Higher". If it's too high, you'll see "Lower".
5. Keep guessing until you find the correct number.
6. The game will show the number of guesses taken.
7. Enter 'e' to exit at any time.

### GUI Version:
1. Run the game, and a window will open.
2. Enter your guess in the text box and click the "Submit" button.
3. Feedback (Higher/Lower) will appear in the window.
4. Once you guess correctly, a pop-up will notify you, and the game will reset for another round.
5. Click "Exit" to close the game.

---

## Project Structure

