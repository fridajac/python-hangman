from correct_guess import correct_guess


def test_should_return_list():
    hidden_word = ["_", "_", "_"]
    answer = "hej"
    guess = "e"
    assert type(correct_guess(hidden_word, guess, answer) == list)
