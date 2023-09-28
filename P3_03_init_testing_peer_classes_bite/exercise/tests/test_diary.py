# File: tests/test_diary.py

# standard import
import pytest

# codebase import
from lib.diary import Diary


"""
Given diary contents
#read returns contents
"""
def test_contents_can_be_read():
    diary_entry = Diary('This is my contents')
    assert diary_entry.read() == 'This is my contents'


"""
Given non-string contents
Diary initialisation raises error "contents must be string"
"""
def test_non_string_contents_raises_error_on_init():
    
    with pytest.raises(Exception) as err:
        Diary(200)

    assert str(err.value) == 'Error: contents must be a string'