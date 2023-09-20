# File: P2_05_test_drive_a_class/tests/test_diary_entry.py
from lib.diary_entry import DiaryEntry
import pytest


"""
Given an empty title and contents, count_words()
Raises error
"""
def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as err:
        entry = DiaryEntry('', '')
    error_message = str(err.value)
    assert error_message == "Diary entries must have a title and contents"



"""
Given a title and contents, we can get a formatted diary entry
#format Returns: "{title}: {contents}"
"""

def test_formatted_entry():
    entry = DiaryEntry('Wednesday', 'Today it is raining.')
    assert entry.format() == 'Wednesday: Today it is raining.'


"""
Given a different title and contents, we can get a formatted diary entry
#format Returns: "{title}: {contents}"
"""

def test_second_formatted_entry():
    entry = DiaryEntry('Friday', 'Today it is sunny.')
    assert entry.format() == 'Friday: Today it is sunny.'


"""
Given a title and contents, count_words() return number of words 
#count_words Returns: count of words (int)
"""
def test_count_words_in_title_and_contents():
    entry = DiaryEntry('Friday', 'Today it is sunny.')
    result = entry.count_words()
    assert result == 5


"""
Given a wpm of 2 and contents of 2 words
#reading_time returns: 1 minute (mins)
"""

def test_reading_time_two_words_two_wpm():
    entry = DiaryEntry('Friday', 'one two')
    result = entry.reading_time(2)
    assert result == 1    


"""
Given a wpm of 2 
and contents of 4 words
#reading_time returns: 2 minutes (mins)
"""

def test_reading_time_four_words_two_wpm():
    entry = DiaryEntry('Friday', 'one two three four')
    result = entry.reading_time(2)
    assert result == 2


"""
Given a wpm of 2 
and contents of 3 words
#reading_time returns: 2 minutes (mins)
"""

def test_reading_time_three_words_two_wpm():
    entry = DiaryEntry('Friday', 'one two three')
    result = entry.reading_time(2)
    assert result == 2



"""
Given a wpm of 0 
#reading_time Raises an error
"""

def test_reading_time_three_words_two_wpm():
    entry = DiaryEntry('Friday', 'one two three')
    with pytest.raises(Exception) as err:
        result = entry.reading_time(0)
    error_message = str(err.value)
    assert error_message == "Cannot calculate reading time with wpm of 0"


"""
Given a wpm of 2
and empty contents 
#reading_time Raises an error
"""

def test_reading_time_three_words_two_wpm():
    entry = DiaryEntry('Friday', 'one two three')
    with pytest.raises(Exception) as err:
        result = entry.reading_time(0)
    error_message = str(err.value)
    assert error_message == "Cannot calculate reading time with wpm of 0"


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


"""
Given a contents of 6 words
and wpm of 2
and minutes of 1
First time, #reading_chunk(2,1) returns 'one two'
Next time, #reading_chunk(1,1) returns 'three four'
Next time, #reading_chunk(2,1) returns 'five six'
"""

def test_reading_chunk_with_two_wpm_and_one_minutes_called_twice():
    entry = DiaryEntry('Friday', 'one two three four five six')
    assert entry.reading_chunk(2, 1) == 'one two'
    assert entry.reading_chunk(1, 1) == 'three'
    assert entry.reading_chunk(2, 1) == 'four five'


"""
Given a contents of six words
If #reading_chunk is called repeatedly
The last chunk is the last words in the text, even if shorter than could be read
The next chunk after that is at the start again
"""
def test_reading_chunk_wraps_around_with_multiple_calls():
    entry = DiaryEntry('Friday', 'one two three four five six')
    assert entry.reading_chunk(2, 2) == 'one two three four'
    assert entry.reading_chunk(2, 2) == 'five six'
    assert entry.reading_chunk(2, 2) == 'one two three four'


"""
Given a contents of six words
If #reading_chunk is called repeatedly with exact ending
The last chunk is the last words in the text
The next chunk after that is at the start again
"""
def test_reading_chunk_wraps_around_with_multiple_calls_with_exact_ending():
    entry = DiaryEntry('Friday', 'one two three four five six')
    assert entry.reading_chunk(2, 2) == 'one two three four'
    assert entry.reading_chunk(2, 1) == 'five six'
    assert entry.reading_chunk(2, 2) == 'one two three four'