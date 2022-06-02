import re


def correct_guess(hidden_word, guess, answer):
    print("Yey! That's right. Your word is now:")
    indexes = [i.start() for i in re.finditer(guess.lower(), answer)]
    for i in indexes:
        hidden_word[i] == guess.lower
    return hidden_word
