from check_level import check_level


def test_zero_should_return_none():
    assert check_level(0) is None


def test_one_should_return_one():
    assert check_level(1) == 1


def test_two_should_return_two():
    assert check_level(2) == 2


def test_three_should_return_three():
    assert check_level(3) == 3


def test_string_should_return_none():
    assert check_level("hej") is None


def test_empty_should_return_none():
    assert check_level("") is None
