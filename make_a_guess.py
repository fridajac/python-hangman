import re


def make_a_guess(hidden_word, guess, answer):
    if len(guess) == 1 and guess in answer:
        indexes = [i.start() for i in re.finditer(guess, answer)]
        for i in indexes:
            hidden_word[i] = guess
        return hidden_word
    else:
        return None
