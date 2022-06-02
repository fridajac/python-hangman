import random

# Start game by invite
wordsLevel1 = ["Summer", "Spice", "Lilly"]
wordsLevel2 = ["Musicplayer", "Slenderman", "Soulmate"]
wordsLevel3 = ["Acquiesce", "Appease", "Circumspect"]


def generate_word(level):
    word = ""
    match level:
        case 1:
            word = random.choice(wordsLevel1)
        case 2:
            word = random.choice(wordsLevel2)
        case 3:
            word = random.choice(wordsLevel3)
    return word


def start_game(name, answer):
    while True:
        guess = input('Guess a letter:')
        if (guess in answer):
            print("Yes!")

def main():
    print("\nWelcome to Hangman game by DataFlair\n")
    name = input("Enter your name: ")
    level = input("Enter level (1-3): ")
    print(f'Hi, {name}' + f'! Welcome to level {level})')
    word = generate_word(level)
    start_game(name, word)

main()
