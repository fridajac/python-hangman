from create_hidden_word import create_hidden_word


def test_should_return_list():
    assert type(create_hidden_word(5)) == list


def test_should_return_():
    hidden_word = create_hidden_word(2)
    assert hidden_word.pop(0) == "_"


def test_should_return_two_():
    hidden_word = create_hidden_word(2)
    assert len(hidden_word) == 2


def test_should_return_ten_():
    hidden_word = create_hidden_word(10)
    assert len(hidden_word) == 10

