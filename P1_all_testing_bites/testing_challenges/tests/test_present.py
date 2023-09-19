# File: test/test_present.py
import pytest 
from lib.present import Present


def test_wrap_and_unwrap():
    """
    When we wrap something, we are able to unwrap it
    """

    present = Present()
    present.wrap('phone')
    assert present.unwrap() == 'phone'


def test_unwrap_empty_present():
    """
    Tests unwrapping empty present returns error.
    """

    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    error_message = str(err.value)
    assert error_message == "No contents have been wrapped."


def test_wrap_when_contents_is_not_none():
    """
    Tests wrapping over already wrapped item returns error.
    """

    present = Present()
    present.wrap('book')
    with pytest.raises(Exception) as err:
        present.wrap('clothes')
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."


def test_wrap_when_contents_is_not_none_does_not_overwrite_present():
    """
    Tests wrapping over already wrapped item does not overwrite original.
    """

    present = Present()
    present.wrap('book')
    with pytest.raises(Exception) as err:
        present.wrap('clothes')
    assert present.unwrap() == 'book'
