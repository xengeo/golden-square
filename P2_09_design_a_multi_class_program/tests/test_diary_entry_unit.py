# File: tests/test_diary_entry_unit.py
import pytest
from lib.diary_entry import DiaryEntry

"""
Given a title and contents,
we see the titel and contents reflected in title and contents properties
"""
def test_initialisation_of_title_contents():
    entry_1 = DiaryEntry('Title1', 'one two')
    assert entry_1.title == 'Title1'
    assert entry_1.contents == 'one two'

"""
Given a title and contents with 4 words,
count_words() returns: int 4
"""
def test_count_words_4_words():
    entry_1 = DiaryEntry('Title1', 'one two three four')
    assert entry_1.count_words() == 4

"""
Given a title and contents with 4 words,
wpm of 2
reading_time() returns: 
"""
def test_reading_time_4_words_2_wpm():
    entry_1 = DiaryEntry('Title1', 'one two three four')
    assert entry_1.reading_time(2) == 2

"""
Test reading time with 0 wpm raises error
"""
def test_reading_time_with_0wpm_raises_error():
    entry = DiaryEntry('title one', 'one two three four')
    with pytest.raises(Exception) as err:
        entry.reading_time(0)
    assert str(err.value) == "wpm cannot be 0"