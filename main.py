import time

from check_level import check_level
from create_hidden_word import create_hidden_word
from generate_answer import generate_answer
from make_a_guess import make_a_guess
from display_hanging_man import display_hanging_man


def play_game(answer):
    nbr_of_tries = 5
    hidden_word = create_hidden_word(len(answer))
    time.sleep(1)
    while True:
        for i in hidden_word:
            print(i, end=' ')
        print()
        guess = input('Enter your guess between a-z').strip().lower()
        result = make_a_guess(hidden_word, guess, answer)
        if result is not None:
            hidden_word = result
            print("Yey! That's right")
            if "_" not in hidden_word:
                print("Good job, you did it! It was " + answer)
                break
        else:
            nbr_of_tries -= 1
            display_hanging_man(nbr_of_tries, answer)
            if nbr_of_tries == 0:
                break


def start_new_game():
    name = input("Enter your name: ")
    while True:
        level = check_level(input("Enter level (1-3): "))
        if level is not None:
            break
        else:
            print("You need to enter a number between 1 -3")

    print(f'Hi, {name}' + f'! Welcome to level {level}. Best of luck!')
    time.sleep(1)
    answer = generate_answer(level)
    play_game(answer)


def main():
    print("\nWelcome to Hangman game!\n")
    time.sleep(1)
    start_new_game()


main()
