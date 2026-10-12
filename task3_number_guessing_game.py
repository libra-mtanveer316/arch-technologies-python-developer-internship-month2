import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have picked a number between 1 and 100. Can you guess it?")

    while True:
        guess = input("Enter your guess: ")

        # make sure the user typed a proper number
        if not guess.isdigit():
            print("That's not a valid number, try again.")
            continue

        guess = int(guess)

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a bigger number.")
        elif guess > secret_number:
            print("Too high! Try a smaller number.")
        else:
            print(f"Correct! The number was {secret_number}.")
            print(f"You got it in {attempts} attempts.")
            break


def main():
    print("=== Number Guessing Game ===")

    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing, bye!")
            break

main()
