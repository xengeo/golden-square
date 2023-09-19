# File: tests/test_make_snippet.py
from lib.make_snippet import make_snippet


"""
A function called make_snippet that takes a string as an argument and 
returns the first five words and then a '...' if there are more than that.
"""


def test_empty_str_returns_empty_str():
    """Tests an empty string returns an empty string"""
    result = make_snippet('')
    assert result == ''


def test_four_words_returns_four_words():
    """"Tests four word string returns same string without '...' on end"""
    result = make_snippet('hello how are you')
    assert result == 'hello how are you'


def test_five_words_returns_five_words():
    """"Tests five word string returns same string without '...' on end"""
    result = make_snippet('one two three four five')
    assert result == 'one two three four five'


def test_six_word_string():
    """"
    Tests six word string returns first five words 
    string with '...' on end
    """

    result = make_snippet('one two three four five six')
    assert result == 'one two three four five...'


def test_six_word_string_delimited_by_commas():
    """"
    Tests six word string delimited by commas returns same string
    """

    result = make_snippet('one,two,three,four,five,six')
    assert result == 'one,two,three,four,five,six'