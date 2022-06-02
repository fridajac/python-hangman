def make_a_guess(guess, answer):
    if len(guess) == 1 and guess.lower() in answer:
        return True
    else:
        return False
