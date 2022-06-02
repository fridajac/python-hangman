import random

# Start game by invite
from check_level import check_level
from generate_word import generate_word


def start_game(name, answer):
    while True:
        guess = input('Guess a letter:')
        if guess in answer:
            print("Yes!")


def main():
    print("\nWelcome to Hangman game by Me\n")
    name = input("Enter your name: ")
    while True:
        level = check_level(input("Enter level (1-3): "))
        if level is not None:
            break
        else:
            print("You need to enter a number between 1 -3")

    print(f'Hi, {name}' + f'! Welcome to level {level}')
    word = generate_word(level)
    start_game(name, word)


main()
