# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import re


def make_a_guess(game_board, guess, answer):
    if len(guess) == 1 and guess in answer:
        indexes = [i.start() for i in re.finditer(guess, answer)]
        for i in indexes:
            game_board[i] = guess
        return game_board
    return None
