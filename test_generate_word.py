from generate_word import generate_word


def test_should_return_str():
    assert type(generate_word(1) == str)


def test_one_should_return_word_in_level1():
    words_level1 = ["Summer", "Spice", "Lilly"]
    assert generate_word(1) in words_level1


def test_two_should_return_word_in_level2():
    words_level2 = ["Musicplayer", "Slenderman", "Soulmate"]
    assert generate_word(2) in words_level2


def test_three_should_return_word_in_level3():
    words_level3 = ["Acquiesce", "Appease", "Circumspect"]
    assert generate_word(3) in words_level3


def test_invalid_value_should_return_false():
    assert generate_word("hej") is None
