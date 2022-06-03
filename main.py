import time

from check_level import check_level
from create_game_board import create_game_board
from generate_secret_word import generate_secret_word
from make_a_guess import make_a_guess
from display_hanging_man import display_hanging_man


def play_game(secret_word, game_board):
    nbr_of_tries = 5
    time.sleep(1)

    while True:
        for i in game_board:
            print(i, end=' ')

        print()
        guess = input('Enter your guess between a-z').strip().lower()
        result = make_a_guess(game_board, guess, secret_word)
        if result is not None:
            game_board = result
            print("Yey! That's right")
            if "_" not in game_board:
                print("Good job, you did it! It was " + secret_word)
                break
        else:
            nbr_of_tries -= 1
            display_hanging_man(nbr_of_tries, secret_word)
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
    secret_word = generate_secret_word(level)
    game_board = create_game_board(len(secret_word))
    play_game(secret_word, game_board)


def main():
    print("\nWelcome to Hangman game!\n")
    time.sleep(1)
    start_new_game()


main()
