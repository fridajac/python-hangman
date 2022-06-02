from make_a_guess import make_a_guess


def test_should_return_list():
    hidden_word = ["_", "_", "_"]
    answer = "hej"
    guess = "e"
    assert type(make_a_guess(hidden_word, guess, answer) == list)


def test_should_return_visible_e():
    assert make_a_guess(["_", "_", "_"], "e", "hej") == ["_", "e", "_"]


def test_should_return_two_visible_e():
    assert make_a_guess(["_", "_", "_", "_", "_"], "e", "speed") == ["_", "_", "e", "e", "_"]


def test_should_return_none():
    assert make_a_guess(["_", "_", "_"], "o", "hej") is None
