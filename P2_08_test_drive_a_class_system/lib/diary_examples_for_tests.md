```python


"""
Initially, there are no diary entries
"""
diary = Diary()
entries = diary.all()
assert entries == []


"""
Add multiple diary entries
# all() returns: list of entry instances
"""
diary = Diary()
entry_1 = DiaryEntry('Entry 1', 'Contents for entry 1')
entry_2 = DiaryEntry('Entry 2', 'Contents for entry 2')
diary.add(entry_1)
diary.add(entry_2)
entries = diary.all()
assert entries == [entry_1, entry_2]


"""
Given some diary entries,
#count_words() returns: (int) total word count for all entries
"""
diary = Diary()
entry_1 = DiaryEntry('Entry 1', 'Contents for entry 1')
entry_2 = DiaryEntry('Entry 2', 'Contents for entry 2')
diary.add(entry_1)
diary.add(entry_2)
assert diary.count_words() == 8


"""
Given no diary entries created
#count_words() returns = 0
"""
diary = Diary()
assert diary.count_words() == 0


"""
Given some diary entries
8 total words
wpm 2
#reading_time() returns: reading time (mins)
"""
diary = Diary()
entry_1 = DiaryEntry('Entry 1', 'Contents for entry 1')
entry_2 = DiaryEntry('Entry 2', 'Contents for entry 2')
diary.add(entry_1)
diary.add(entry_2)
assert diary.reading_time(2) == '4 minutes'


"""
Given some diary entries of different lengths
wpm = 2
minutes = 4
#find_best_entry_for_reading_time() returns the best suited entry
"""
diary = Diary()
entry_1 = DiaryEntry('Title 1', 'Contents for entry one') # 4 words
entry_2 = DiaryEntry('Title 2', 'Some other contents for entry two') # 6 words
diary.add(entry_1)
diary.add(entry_2)
assert diary.find_best_entry_for_reading_time(wpm=2, minutes=4) == entry_1


```



