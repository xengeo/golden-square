# File: tests/test_integrated_diary.py

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
    assert diary.all() == [diary_entry1]