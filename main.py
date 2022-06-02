# Start game by invite
from check_level import check_level
from correct_guess import correct_guess
from create_hidden_word import create_hidden_word
from generate_answer import generate_answer
from make_a_guess import make_a_guess


def start_game(answer):
    hidden_word = create_hidden_word(len(answer))

    print(answer)
    while True:
        for i in hidden_word:
            print(i, end=' ')
        print()
        guess = input('Guess a letter a-z')
        if make_a_guess(guess, answer):
            correct_guess(hidden_word, guess, answer)
        else:
            print("Nope, go again!")


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
    answer = generate_answer(level)
    start_game(answer)


main()
