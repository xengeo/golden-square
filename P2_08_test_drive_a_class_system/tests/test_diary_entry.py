#  File: tests/test_diary_entry.py
from lib.diary import DiaryEntry


"""
Given an entry of 4 words
#count_words returns: 4 (int) 
"""
def test_count_words_return_four():
    entry_one = DiaryEntry('title 1', 'Contents for entry one')
    assert entry_one.count_words() == 4


"""
Given a contents of 6 words
and wpm of 2
and minutes of 1
#reading_chunk returns the first 2 words
"""

def test_reading_chunk_with_two_wpm_and_one_minutes():
    entry = DiaryEntry('Friday', 'one two three four five six')
    result = entry.reading_chunk(2, 1)
    assert result == 'one two'


"""
Given a contents of 6 words
and wpm of 2
and minutes of 2
#reading_chunk returns the first 4 words
"""

def test_reading_chunk_with_two_wpm_and_two_minutes():
    entry = DiaryEntry('Friday', 'one two three four five six')
    result = entry.reading_chunk(2, 2)
    assert result == 'one two three four'


# could add more tests if more time