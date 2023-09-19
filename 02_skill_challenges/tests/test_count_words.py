# File: tests/test_count_words.py

from lib.count_words import count_words

"""
A function called count_words 
Input: string 
Returns: Number of words in string (integer)
"""


def test_empty_string_returns_zero():
    """
    Tests empty string returns 0.
    """
    result = count_words('')
    assert result == 0

def test_one_word_string_returns_one():
    """
    Tests one word string returns 1.
    """
    result = count_words('one')
    assert result == 1

def test_two_word_string_returns_two():
    """
    Tests 2 word string returns 2.
    """
    result = count_words('one two')
    assert result == 2

def test_comma_delimited_string_of_words():
    """
    Tests string of 4 words delimited by commas returns 1.
    """
    result = count_words('one,two,three,four')
    assert result == 1