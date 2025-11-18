"""
Bulls and cows game

author: Jana Cápíková
email: capikovajana@gmail.com
"""

import random
import time

# Constants for game configuration
DIGITS_COUNT = 4
MIN_NUMBER = 1000
MAX_NUMBER = 9999
SEPARATOR = "-" * 47


def generate_secret_number() -> str:
    # Generate a random number with unique digits and no leading zero.
    while True:
        number = str(random.randint(MIN_NUMBER, MAX_NUMBER))
        if len(set(number)) == len(number):
            return number


def validate_guess(guess: str, length: int) -> tuple[bool, str]:
    """
    Validate user input.

    Returns (is_valid, error_message). If is_valid is True,
    error_message is an empty string.
    """
    if len(guess) != length:
        return False, f"Please enter a {length}-digit number."

    if not guess.isdigit():
        return False, "Only numeric characters are allowed."

    if guess[0] == "0":
        return False, "Please enter a number that does not begin with 0."

    if len(set(guess)) != len(guess):
        return False, "The number must not contain any repeated digits."

    return True, ""


def evaluate_guess(secret: str, guess: str) -> tuple[int, int]:
    """
    Return the number of bulls and cows for the given guess.

    Bull  = correct digit in the correct position.
    Cow   = correct digit, but in a different position.
    """
    bulls = 0
    cows = 0

    # Go through all digits in the guess together with their index
    for index, digit in enumerate(guess):
        # If the digit matches the secret digit at the same position -> bull
        if digit == secret[index]:
            bulls += 1
        # If the digit is in the secret number, but at a different position -> cow
        elif digit in secret:
            cows += 1

    return bulls, cows


def format_word(count: int, singular: str, plural: str) -> str:
    # Return correct singular/plural word based on count.
    return singular if count == 1 else plural


def print_intro() -> None:
    # Print the introduction text of the game.
    print("Hi there!")
    print(SEPARATOR)
    print(f"I've generated a random {DIGITS_COUNT} digit number for you.")
    print("Let's play a bulls and cows game.")
    print(SEPARATOR)


def play_game() -> None:
    # Run one round of the Bulls and Cows game.
    secret_number = generate_secret_number()
    secret_length = len(secret_number)
    attempts = 0
    start_time = time.time()

    # Main game loop - repeats until the player guesses the secret number
    while True:
        guess = input("Enter a number: ")
        attempts += 1

        is_valid, error_message = validate_guess(guess, secret_length)
        if not is_valid:
            print(error_message)
            continue

        bulls, cows = evaluate_guess(secret_number, guess)

        bull_word = format_word(bulls, "bull", "bulls")
        cow_word = format_word(cows, "cow", "cows")

        print(f"{bulls} {bull_word}, {cows} {cow_word}")
        print(SEPARATOR)

        if bulls == secret_length:
            elapsed_time = round(time.time() - start_time, 2)
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print(f"Time: {elapsed_time} seconds")
            print(SEPARATOR)
            print("That's amazing!")
            break


def main() -> None:
    # Program entry point.
    print_intro()
    play_game()


if __name__ == "__main__":
    main()