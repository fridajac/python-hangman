import random

words_level1 = ["Summer", "Spice", "Lilly"]
words_level2 = ["Musicplayer", "Slenderman", "Soulmate"]
words_level3 = ["Acquiesce", "Appease", "Circumspect"]


def generate_word(level):
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
