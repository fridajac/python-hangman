
# Start game by invite
from check_level import check_level
from generate_answer import generate_answer
from make_a_guess import make_a_guess


def create_hidden_word(number):
    hidden_word = []
    for element in number:
        hidden_word.append("_")
    return hidden_word

def start_game(answer):
    hidden_word = create_hidden_word(len(answer))
    print(hidden_word)
    guess = input('Guess a letter a-z')
    if make_a_guess(guess, answer):
        print("Yey! That's right. Your word is now:")




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
