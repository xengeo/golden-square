# File: tests/test_integrated_diary.py

# standard imports
import pytest

# my imports
from lib.diary import Diary
from lib.diary_entry import DiaryEntry


"""
Test add method with 2 valid entires.
All method returns list with added entries included.
"""
def test_add_diary_entry_returns_list_of_entries():
    diary = Diary()
    diary_entry1 = DiaryEntry('Title1', 'one two three')
    diary.add_entry(diary_entry1)
    assert diary.list_all_entries() == [diary_entry1]


"""
Test add invalid entry of type string
Raises error
"""
def test_add_invalid_entry_type_raises_error():
    diary = Diary()
    diary_entry1 = 'Entry1'
    with pytest.raises(Exception) as err:
        diary.add_entry(diary_entry1)
    error_message = str(err.value)
    assert error_message == "Entry must be DiaryEntry object"


"""
Test find the best entry given two entries with
2 words length and 4 words length 
with 2wpm and 1min
returns 
"""
def test_get_best_entry_for_reading_time_2wpm_1min():
    diary = Diary()
    diary_entry1 = DiaryEntry('Title1', 'one two')
    diary_entry2 = DiaryEntry('Title2', 'three four five six')
    diary.add_entry(diary_entry1)
    diary.add_entry(diary_entry2)
    assert diary.find_best_entry_for_reading_time(2, 1) == diary_entry1


"""Given and 0minutes find the best entry returns an error"""
def test_find_best_entry_raises_error_for_test_0mins():
    diary = Diary()
    diary_entry1 = DiaryEntry('Title1', 'one two')
    diary_entry2 = DiaryEntry('Title2', 'three four five six')
    diary.add_entry(diary_entry1)
    diary.add_entry(diary_entry2)
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(1, 0)
    assert str(err.value) == "Minutes can't be 0"


"""Given and 0 wpm find the best entry returns an error"""
def test_find_best_entry_raises_error_for_test_0wpm():
    diary = Diary()
    diary_entry1 = DiaryEntry('Title1', 'one two')
    diary_entry2 = DiaryEntry('Title2', 'three four five six')
    diary.add_entry(diary_entry1)
    diary.add_entry(diary_entry2)
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(0, 1)
    assert str(err.value) == "wpm cannot be 0"