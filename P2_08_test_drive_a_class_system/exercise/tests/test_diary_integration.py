# File: tests/test_diary_integration.py
from lib.diary import Diary, DiaryEntry
import pytest


"""
Initially, there are no diary entries
"""
def test_no_diary_entries_returns_empty_list():
    diary = Diary()
    entries = diary.all()
    assert entries == []


"""
Add multiple diary entries
# all() returns: list of entry instances
"""
def test_two_diary_entries_returns_list_of_entry_instances():
    diary = Diary()
    entry_one = DiaryEntry('Entry 1', 'Contents for entry one')
    entry_two = DiaryEntry('Entry 2', 'Contents for entry two')
    diary.add(entry_one)
    diary.add(entry_two)
    entries = diary.all()
    assert entries == [entry_one, entry_two]


"""
Given some diary entries,
#count_words() returns: (int) total word count for all entries
"""
def test_count_words_for_two_entries():
    diary = Diary()
    entry_one = DiaryEntry('Entry 1', 'Contents for entry one')
    entry_two = DiaryEntry('Entry 2', 'Contents for entry two')
    diary.add(entry_one)
    diary.add(entry_two)
    assert diary.count_words() == 8


"""
Given no diary entries created
#count_words() returns = 0
"""
def test_count_words_returns_zero_for_no_entries():
    diary = Diary()
    assert diary.count_words() == 0


"""
Given some diary entries
8 total words
wpm 2
#reading_time() returns: reading time (mins)
"""
def test_reading_time_two_wpm_two_entries():
    diary = Diary()
    entry_1 = DiaryEntry('Entry 1', 'Contents for entry one')
    entry_2 = DiaryEntry('Entry 2', 'Contents for entry two')
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == '4 minutes'


"""
Given some diary entries
and wpm 0
#reading_time() rasies error 'Cannot calculate reading time with wpm of 0'
"""
def test_reading_time_zero_wpm_raises_error():
    diary = Diary()
    entry_1 = DiaryEntry('Entry 1', 'Contents for entry one')
    entry_2 = DiaryEntry('Entry 2', 'Contents for entry two')
    diary.add(entry_1)
    diary.add(entry_2)
    with pytest.raises(Exception) as e:
        diary.reading_time(0) == '4 minutes' 
    error_message = str(e.value)
    assert error_message == 'Cannot calculate reading time with wpm of 0'


"""
Given some diary entries of different lengths
wpm = 2
minutes = 4
#find_best_entry_for_reading_time() returns the best suited entry
"""
def test_best_entry_for_two_wpm_and_four_minutes():
    diary = Diary()
    entry_1 = DiaryEntry('Title 1', 'Contents for entry one') # 4 words
    entry_2 = DiaryEntry('Title 2', 'Some other contents for entry two') # 6 words
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(wpm=2, minutes=4) == entry_1


# Test for checking reading time and best entry when diary_entries is empty
# add more tests if time