# File: lib/diary.py
import math

class Diary:
    def __init__(self):
        self._diary_entries = []

    def add_entry(self, entry) -> None:
        """        
        Parameters: entry: an instance of DiaryEntry
        Returns:    Nothing
        Side-effects:   Adds the entry to the entries list
        """
        # Add check to make sure entry is an instance of DiaryEntry
        self._diary_entries.append(entry)

    def list_all_entries(self) -> list:
        """Returns: A list of instances of DiaryEntry"""
        return self._diary_entries

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
            
