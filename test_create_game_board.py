from create_game_board import create_game_board


def test_should_return_list():
    assert type(create_game_board(5)) == list


def test_should_return_():
    hidden_word = create_game_board(2)
    assert hidden_word.pop(0) == "_"


def test_should_return_two_():
    hidden_word = create_game_board(2)
    assert len(hidden_word) == 2


def test_should_return_ten_():
    hidden_word = create_game_board(10)
    assert len(hidden_word) == 10

