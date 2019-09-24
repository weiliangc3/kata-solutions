
from text_justification import justify_text

def test_when_given_two_words():
    result = justify_text(input = "hello wei", expected_width = 12)
    print(result)
    assert result == "hello    wei"

def test_when_given_a_long_string():
    result = justify_text(input = "hello wei you got this right yes", expected_width = 12)
    print(result)
    assert result == "hello    wei\nyou got this\nright    yes"

def test_when_given_variable_widths():
    result = justify_text(input = "hello wei you got this right yes", expected_width = 14)
    print(result)
    assert result == "hello  wei you\ngot this right\nyes"

def test_when_given_a_very_large_word():
    result = justify_text(input = "hello wei you got this right yesyoudoright yes", expected_width = 14)
    print(result)
    assert result == "hello  wei you\ngot this right\nyesyoudoright\nyes"