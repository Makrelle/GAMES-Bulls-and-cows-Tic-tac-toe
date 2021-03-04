# 2nd project - Bulls and Cows
import random


SEPARATOR = "-" * 50
print("""Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(SEPARATOR)


def generate_number() -> list:
    number = []
    while len(number) < 4:
        num = random.randrange(0, 10)
        if num not in number:
            number.append(num)
    return number


def check_number(number: list, guessed_number: str) -> tuple:
    bulls, cows = 0, 0
    for i, num in enumerate(number):
        if num == int(guessed_number[i]):
            bulls += 1
        if str(num) in guessed_number:
            cows += 1
    cows -= bulls
    return bulls, cows


def print_bulls_and_cows(bulls: int, cows: int):
    p_bulls = str(bulls) + " bull" if bulls == 1 else str(bulls) + " bulls"
    p_cows = str(cows) + " cow" if cows == 1 else str(cows) + " cows"
    print(f"{p_bulls}, {p_cows}", SEPARATOR, sep="\n")


def guess_number():
    while True:
        guessed_number = input("Enter a number ")
        if len(guessed_number) == 4 and guessed_number.isnumeric():
            return guessed_number
        print("Please enter 4 digit number! ")


def main():
    number = generate_number()
    guesses = 0
    while True:
        bulls, cows = check_number(number, guess_number())
        guesses += 1
        if bulls == 4:
            break
        print_bulls_and_cows(bulls, cows)
    print(f"Correct! You've guessed the right number in {guesses} guesses.")


while True:
    main()
    play_again = input("Do you want to play again? Press 'y' to continue.. ")
    if play_again.lower() == "y":
        continue
    else:
        print("Thank you for your game! ")
        exit()
