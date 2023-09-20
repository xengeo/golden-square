# File: tests/test_includes_todo.py
from lib.includes_todo import includes_todo
import pytest


"""
Given a string containing only '#TODO'
Returns: 'This text includes a #TODO.'
"""

def test_only_todo():
    result = includes_todo('#TODO')
    assert result == 'This text includes a #TODO.'


"""
Given an empty string
Returns: "This text does not include a #TODO."
"""

def test_empty_string():
    result = includes_todo('')
    assert result == 'This text does not include a #TODO.'



"""
Given a long text with #TODO in it
Returns: "This text includes a #TODO."
"""

def test_long_text_with_todo():
    text = "hello " * 100 + '#TODO ' + "bye " * 100
    result = includes_todo(text)
    assert result == "This text includes a #TODO."


"""
Given a long text without #TODO in it
Returns: "This text does not include a #TODO."
"""

def test_long_text_without_todo():
    text = "hello " * 100 + "bye " * 100
    result = includes_todo(text)
    assert result == "This text does not include a #TODO."



"""
Given the wrong data type
Returns: "Error: wrong data type submitted, please input text/strings only."
"""

def test_wrong_data_type_submitted():
    with pytest.raises(Exception) as err:
        includes_todo(1234)
    error_message = str(err.value)
    assert error_message == "Error: wrong data type submitted, please input text/strings only."