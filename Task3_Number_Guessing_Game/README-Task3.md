# NUMBER GUESSING GAME

A console-based Python program where the computer picks a secret number between 1 and 100 and the player tries to guess it. Built during Month 2 of my Python Development internship at **Arch Technologies**.

**Repository:** https://github.com/libra-mtanveer316/arch-technologies-python-developer-internship-month2

---

## Quick Start

### 1. Install requirement

No external packages needed — this program uses only Python's standard library.

```
pip install -r requirements.txt
```

### 2. Run the program

```
python task3_number_guessing_game.py
```

---

## How It Works

```
Start
  |
  v
Print welcome message
  |
  v
Computer picks a secret number (random.randint(1, 100))
  |
  v
Ask the player for a guess
  |
  v
Not a number, or outside 1-100? -> show a message and ask again
  |
  v
Count the attempt
  |
  v
guess < secret -> "Too low!"   guess > secret -> "Too high!"
  |
  v
Guess is correct -> show the number and total attempts
  |
  v
Ask: Play again? (yes/no)
  |
  v
"yes" -> loop back and pick a new number
anything else -> print goodbye message and exit
```

---

## Concepts Applied

| # | Concept |
|---|---------|
| 1 | `random` module |
| 2 | Functions |
| 3 | `while` loops |
| 4 | Conditional logic (`if` / `elif` / `else`) |
| 5 | f-strings |
| 6 | User input handling and validation |

---

## Example Session

```
=== Number Guessing Game ===

I have picked a number between 1 and 100. Can you guess it?
Enter your guess: 50
Too high! Try a smaller number.
Enter your guess: abc
That's not a valid number, try again.
Enter your guess: 25
Too high! Try a smaller number.
Enter your guess: 10
Too low! Try a bigger number.
Enter your guess: 18
Correct! The number was 18.
You got it in 4 attempts.

Do you want to play again? (yes/no): no
Thanks for playing, bye!
```

---

## Notes

- `random.randint(1, 100)` is used because it includes both 1 and 100, so every number in the range has a fair chance of being picked.
- Input is checked with `.isdigit()` before converting to an integer, so typing letters doesn't crash the program.
- Invalid guesses (letters or numbers outside 1-100) are not counted as attempts, so the attempt counter only reflects real guesses.
- The play-again answer is cleaned with `.strip().lower()` so `Yes`, `yes`, or a stray space all behave the same way.

---

## Files

| File | Purpose |
|------|---------|
| `task3_number_guessing_game.py` | Main program — run this |
| `requirements.txt` | Dependency list (none — standard library only) |
| `README-Task3.md` | This file |

## Author

**Muhammad Tanveer**
Python Development Intern — Arch Technologies
