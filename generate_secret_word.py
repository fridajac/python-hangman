# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import random

words_level1 = ["summer", "spice", "lilly"]
words_level2 = ["musicplayer", "slenderman", "soulmate"]
words_level3 = ["acquiesce", "appease", "circumspect"]


def generate_secret_word(level):
    match level:
        case 1:
            secret_word = random.choice(words_level1)
        case 2:
            secret_word = random.choice(words_level2)
        case 3:
            secret_word = random.choice(words_level3)
        case _:
            return None
    return secret_word
