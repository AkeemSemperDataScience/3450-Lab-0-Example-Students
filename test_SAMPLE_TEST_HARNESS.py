import pytest
from quiz_0_answer_sheet import(
    numberAdder,
    vowelsInString
    )

@pytest.mark.parametrize("input1, input2, expected", [
    (1, 2, 3),
    (-56, 22, -34),
    (0, 0, 0),
    (100, 200, 300),
    (1.5, 2.5, 4.0),
    (1, -1, 0),]
)
def test_numberAdder(input1, input2, expected):
    assert numberAdder(input1, input2) == expected

@pytest.mark.parametrize("input, expected", [
    ("hello", 2),
    ("aeiou", 5),
    ("", 0),
    ("xyz", 0),
    ("aeiouy", 6),]
)
def test_vowelsInString(input, expected):
    assert vowelsInString(input) == expected
