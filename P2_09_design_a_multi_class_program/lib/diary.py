# File: lib/diary.py

from lib.diary_entry import DiaryEntry

class Diary:
    def __init__(self):
        self._diary_entries = []

    def add_entry(self, entry) -> None:
        """        
        Parameters: entry: an instance of DiaryEntry
        Returns:    Nothing
        Side-effects:   Adds the entry to the entries list
        """
        if not isinstance(entry, DiaryEntry):
            raise Exception("Entry must be DiaryEntry object")
        
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
        if minutes == 0:
            raise Exception("Minutes can't be 0")
        for entry in self._diary_entries:
            if entry.reading_time(wpm) <= minutes:
                return entry
            
    def list_all_contacts(self):
        """
        For each diary entry, retreive the names and their respective phone numbers
        Returns: a list of dicts
        """
        pass
            
