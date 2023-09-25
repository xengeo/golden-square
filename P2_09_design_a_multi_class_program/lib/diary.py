# File: lib/diary.py
import math

class Diary:
    def __init__(self):
        self._diary_entries = []
        self._task_list = []

    def add_diary_entry(self, entry) -> None:
        """        
        Parameters: entry: an instance of DiaryEntry
        Returns:    Nothing
        Side-effects:   Adds the entry to the entries list
        """
        # Add check to make sure entry is an instance of DiaryEntry
        self._diary_entries.append(entry)

    def add_task_entry(self, entry) -> None:
        """        
        Parameters: entry: an instance of DiaryEntry
        Returns:    Nothing
        Side-effects:   Adds the entry to the entries list
        """
        # Add check to make sure entry is an instance of DiaryEntry
        self._diary_entries.append(entry)

    def all(self) -> list:
        """Returns: A list of instances of DiaryEntry"""
        return self._diary_entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total_words = 0
        for entry in self._diary_entries:
            total_words += entry.count_words() 
        return total_words
        

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        total_reading_time = 0
        for entry in self._diary_entries:
            total_reading_time += entry.reading_time(wpm) 

        return f"{total_reading_time} minutes"

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.

        for entry in self._diary_entries:
            if entry.reading_time(wpm) <= minutes:
                return entry
            
