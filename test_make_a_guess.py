from make_a_guess import make_a_guess


def test_should_return_false():
    assert make_a_guess("a", "hej") is False


def test_should_return_true():
    assert make_a_guess("h", "hej") is True


def test_empty_guess_should_return_false():
    assert make_a_guess("", "hej") is False


def test_empty_guess_should_return_false():
    assert make_a_guess("hallå", "hej") is False


def test_whole_word_should_return_false():
    assert make_a_guess("hej", "hej") is False


def test_capital_letter_should_return_true():
    assert make_a_guess("S", "summer") is True
