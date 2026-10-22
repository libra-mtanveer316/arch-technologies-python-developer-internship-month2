
import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have picked a number between 1 and 100. Can you guess it?")

    while True:
        guess = input("Enter your guess: ").strip()

        # make sure the user typed a proper whole number
        try:
            guess = int(guess)
        except ValueError:
            print("That's not a valid number, try again.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a bigger number.")
        elif guess > secret_number:
            print("Too high! Try a smaller number.")
        else:
            word = "attempt" if attempts == 1 else "attempts"
            print(f"Correct! The number was {secret_number}.")
            print(f"You got it in {attempts} {word}.")
            break


def main():
    print("=== Number Guessing Game ===")

    try:
        while True:
            play_game()
            again = input("\nDo you want to play again? (yes/no): ").strip().lower()
            if again != "yes":
                print("Thanks for playing, bye!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nThanks for playing, bye!")


if __name__ == "__main__":
    main()
