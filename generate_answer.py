import random

words_level1 = ["summer", "spice", "lilly"]
words_level2 = ["musicplayer", "slenderman", "soulmate"]
words_level3 = ["acquiesce", "appease", "circumspect"]


def generate_answer(level):
    match level:
        case 1:
            word = random.choice(words_level1)
        case 2:
            word = random.choice(words_level2)
        case 3:
            word = random.choice(words_level3)
        case _:
            return None
    return word
