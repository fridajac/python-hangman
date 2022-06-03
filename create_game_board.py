# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# flake8 --disable-noqa dir/: disable=W391

def create_game_board(number):
    hidden_word = []
    for i in range(number):
        hidden_word.append('_')
    return hidden_word
